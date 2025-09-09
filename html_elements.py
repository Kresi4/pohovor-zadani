from html_render import HTMLElement

class Html(HTMLElement):
    def __init__(self, **attrs):
        super().__init__("html", "", **attrs)

    def render(self, indent=0):
        return "<!DOCTYPE html>\n" + super().render(indent)


class Head(HTMLElement):
    def __init__(self, **attrs):
        super().__init__("head", "", **attrs)


class Body(HTMLElement):
    def __init__(self, **attrs):
        super().__init__("body", "", **attrs)


class Title(HTMLElement):
    def __init__(self, content, **attrs):
        super().__init__("title", content, **attrs)


class Input(HTMLElement):
    def __init__(self, type="text", **attrs):
        super().__init__("input", "", **attrs)
        self.attrs["type"] = type


class Select(HTMLElement):
    def __init__(self, **attrs):
        super().__init__("select", "", **attrs)

    def add_option(self, text, value=None, selected=False):
        option_attrs = {"value": value or text}
        if selected:
            option_attrs["selected"] = "selected"
        self.add_child(HTMLElement("option", text, **option_attrs))


class Anchor(HTMLElement):
    def __init__(self, content, **attrs):
        super().__init__("a", content, **attrs)


class Image(HTMLElement):
    def __init__(self, src, alt="", **attrs):
        if not src:
            raise ValueError("Image requires a 'src' attribute")
        super().__init__("img", "", **attrs)
        self.attrs["src"] = src
        self.attrs["alt"] = alt


class Div(HTMLElement):
    def __init__(self, content="", **attrs):
        super().__init__("div", content, **attrs)


class Form(HTMLElement):
    def __init__(self, **attrs):
        super().__init__("form", "", **attrs)

    def add_input(self, type, name, value=""):
        self.add_child(Input(type=type, name=name, value=value))
