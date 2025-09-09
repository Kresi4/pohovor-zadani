from abc import ABC

class Node(ABC):
    def render(self, indent=0):
        raise NotImplementedError

    def __str__(self):
        return self.render()


class TextNode(Node):
    def __init__(self, text):
        self.text = str(text)

    def render(self, indent=0):
        return " " * indent + self.text


class HTMLElement(Node):
    self_closing_tags = {"input", "img", "br", "hr", "meta", "link"}

    def __init__(self, tag, content="", children=None, **attrs):
        self.tag = tag
        self.content = content
        self.attrs = attrs
        self.children = children or []

    def add_child(self, child):
        if isinstance(child, str):
            child = TextNode(child)
        self.children.append(child)

    def render_attrs(self):
        return " ".join(f'{k}="{v}"' for k, v in self.attrs.items())

    def render(self, indent=0):
        spaces = " " * indent
        attr_str = self.render_attrs()
        attr_str = f" {attr_str}" if attr_str else ""

        if self.tag in self.self_closing_tags:
            return f"{spaces}<{self.tag}{attr_str} />"

        if self.children:
            inner = "\n".join(child.render(indent + 2) for child in self.children)
            return f"{spaces}<{self.tag}{attr_str}>{self.content}\n{inner}\n{spaces}</{self.tag}>"
        else:
            return f"{spaces}<{self.tag}{attr_str}>{self.content}</{self.tag}>"
