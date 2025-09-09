# OOP HTML Generator

Tento projekt demonstruje objektovou reprezentaci vybraných HTML elementů v jazyce **Python** pomocí principů objektově orientovaného programování (OOP). Umožňuje vytvářet HTML struktury programově, například jednoduché formuláře, a vypisovat je jako validní HTML kód.

## Obsah projektu

- **Třídy pro HTML elementy:** `Input`, `Select`, `Anchor` (`a`), `Image` (`img`), `Div`, `Form` a další.
- **Abstrakce:** Všechny elementy dědí z základní abstraktní třídy, což zajišťuje rozšiřitelnost a čistý kód.
- **Renderování:** Každý objekt umí vygenerovat svůj HTML zápis pomocí metody `render()`.
- **Ukázka použití:** Sestavení a výpis jednoduchého formuláře.

## Jak to funguje

1. **Vytváření elementů:**
   ```python
   input_field = Input(type="text", name="username")
   select_field = Select(name="vyber")
   select_field.add_option("Možnost 1", "1")
   select_field.add_option("Možnost 2", "2", selected=True)
   link = Anchor("Klikněte zde", href="https://example.com")
   image = Image(src="logo.png", alt="Logo")
   div_box = Div("Text v boxu", class_="box")
   ```

2. **Sestavení formuláře:**
   ```python
   form = Form(action="/submit", method="POST")
   form.add_child(input_field)
   form.add_child(select_field)
   form.add_child(link)
   form.add_child(image)
   form.add_child(div_box)
   form.add_child(Input(type="submit", value="Odeslat"))
   ```

3. **Výpis HTML:**
   ```python
   print(form.render())
   ```

## Jak spustit

1. Stáhněte projekt.
2. Ujistěte se, že máte Python 3.x.
3. V hlavním souboru najdete ukázku generování HTML formuláře.
4. Spusťte soubor:
   ```bash
   python main.py
   ```
   Výsledek bude vypsán na konzoli.

## Principy návrhu

- **Rozšiřitelnost:** Nové HTML elementy lze jednoduše přidat jako nové třídy.
- **Robustnost:** Povinné atributy jsou validovány (např. `src` u obrázků).
- **Čistý kód:** Každá třída má jasně definovanou odpovědnost.

## Ukázka výstupu

```html
<form action="/submit" method="POST">
  <input type="text" name="username" />
  <select name="vyber">
    <option value="1">Možnost 1</option>
    <option value="2" selected="selected">Možnost 2</option>
  </select>
  <a href="https://example.com">Klikněte zde</a>
  <img src="logo.png" alt="Logo" />
  <div class="box">Text v boxu</div>
  <input type="submit" value="Odeslat" />
</form>
```

## Licence

MIT

## Autor

Kresi4  
[GitHub](https://github.com/Kresi4)
