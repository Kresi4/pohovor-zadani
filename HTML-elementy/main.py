from html_elements import *

html = Html()
head = Head()
head.add_child(Title("Ukázkový formulář"))
body = Body()

form = Form(action="/submit", method="POST")
form.add_input("text", "username")
form.add_input("password", "password")
form.add_child(Div("Vyberte možnost:"))

select = Select(name="vyber")
select.add_option("První", "1")
select.add_option("Druhá", "2", selected=True)
form.add_child(select)

form.add_child(Input(type="submit", value="Odeslat"))

body.add_child(form)

html.add_child(head)
html.add_child(body)


print(html.render())
