--Seznam lidí, kteří si půjčili film v posledním roce
SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    a.address || ', ' || ci.city || ', ' || a.postal_code || ', ' || co.country AS full_address
FROM 
    rental r
JOIN 
    customer c ON r.customer_id = c.customer_id
JOIN 
    address a ON c.address_id = a.address_id
JOIN
	city ci ON a.city_id = ci.city_id
JOIN
	country co ON ci.country_id = co.country_id
WHERE 
    r.rental_date >= (CURRENT_DATE - INTERVAL '1 year');


--Počet filmů v jednotlivých kategoriích
SELECT 
    cat.name AS category,
    COUNT(film.film_id) AS film_count
FROM 
    category cat
JOIN 
    film_category fc ON cat.category_id = fc.category_id
JOIN 
    film ON fc.film_id = film.film_id
GROUP BY 
    cat.name
ORDER BY 
    film_count DESC;


--Výpočet pokuty
SELECT
    r.rental_id,
    f.title,
    c.first_name || ' ' || c.last_name AS customer_name,
    CASE
        WHEN r.return_date IS NOT NULL THEN
            DATE_PART('day', r.return_date - (r.rental_date + INTERVAL '14 days'))
        ELSE
            DATE_PART('day', NOW() - (r.rental_date + INTERVAL '14 days'))
    END AS days_late,
    CASE
        WHEN r.return_date IS NOT NULL THEN
            ROUND(
                CAST(
                    GREATEST(0, DATE_PART('day', r.return_date - (r.rental_date + INTERVAL '14 days')) * (f.rental_rate * 0.01))
                    AS numeric
                ),
                2
            )
        ELSE
            ROUND(
                CAST(
                    GREATEST(0, DATE_PART('day', NOW() - (r.rental_date + INTERVAL '14 days')) * (f.rental_rate * 0.01))
                    AS numeric
                ),
                2
            )
    END AS fine
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE
    (
        (r.return_date IS NOT NULL AND DATE_PART('day', r.return_date - (r.rental_date + INTERVAL '14 days')) > 0)
        OR
        (r.return_date IS NULL AND DATE_PART('day', NOW() - (r.rental_date + INTERVAL '14 days')) > 0)
    );


--Počet vytvořených zápůjček dle prodejny, zaměstnance a roku
SELECT 
    st.store_id,
    s.staff_id,
    s.first_name || ' ' || s.last_name AS staff_name,
    EXTRACT(YEAR FROM r.rental_date) AS year,
    COUNT(r.rental_id) AS rentals_count
FROM rental r
JOIN staff s ON r.staff_id = s.staff_id
JOIN store st ON s.store_id = st.store_id
GROUP BY s.staff_id, s.first_name, s.last_name, st.store_id, year
ORDER BY st.store_id, s.staff_id, year;


--Aktualizace vytvořených zápůjček zaměstnanci přes view
CREATE OR REPLACE VIEW staff_rental_stats AS
SELECT 
    st.store_id,
	s.staff_id,
    s.first_name || ' ' || s.last_name AS staff_name,
    EXTRACT(YEAR FROM r.rental_date) AS year,
    COUNT(r.rental_id) AS rentals_count
FROM rental r
JOIN staff s ON r.staff_id = s.staff_id
JOIN store st ON s.store_id = st.store_id
GROUP BY s.staff_id, st.store_id, year
ORDER BY st.store_id, s.staff_id, year;


--Aktualizace vytvořených zápůjček zaměstnanci přes tabulku
INSERT INTO staff_rental_stats (store_id, staff_id, year, rental_count)
SELECT
    st.store_id,
    s.staff_id,
    EXTRACT(YEAR FROM r.rental_date) AS year,
    COUNT(r.rental_id) AS rental_count
FROM rental r
JOIN staff s ON r.staff_id = s.staff_id
JOIN store st ON s.store_id = st.store_id
GROUP BY st.store_id, s.staff_id, year
ON CONFLICT (store_id, staff_id, year)
DO UPDATE SET rental_count = EXCLUDED.rental_count;


--Funkce pro přidání filmu
CREATE OR REPLACE FUNCTION add_new_film(
    p_title TEXT,
    p_description TEXT,
    p_release_year INT,
    p_language_id INT,
    p_rental_duration INT,
    p_rental_rate NUMERIC,
    p_length INT,
    p_replacement_cost NUMERIC,
    p_rating TEXT
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO film (
        title,
        description,
        release_year,
        language_id,
        rental_duration,
        rental_rate,
        length,
        replacement_cost,
        rating,
        last_update
    ) VALUES (
        p_title,
        p_description,
        p_release_year,
        p_language_id,
        p_rental_duration,
        p_rental_rate,
        p_length,
        p_replacement_cost,
        p_rating,
        NOW()
    );
END;
$$ LANGUAGE plpgsql;
