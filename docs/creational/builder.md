---
title: Creational Design Patterns
description: Creational design patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.
---

# Creational Design Patterns

::: src.creational
::: src.creational.builder

## Source Code
``` py linenums="1" title="src/creational/builder.py"
class HTMLComponent:
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return f"<div>{self.content}</div>"


class CSSComponent:
    def __init__(self, style: str):
        self.style = style

    def render(self) -> str:
        return f".element {{ {self.style} }}"


class CodeBuilder:
    def __init__(self):
        self.html_components = []
        self.css_components = []

    def add_html(self, content: str) -> 'CodeBuilder':
        self.html_components.append(HTMLComponent(content))
        return self

    def add_css(self, style: str) -> 'CodeBuilder':
        self.css_components.append(CSSComponent(style))
        return self

    def build_html(self) -> str:
        return "\n".join(component.render() for component in self.html_components)

    def build_css(self) -> str:
        return "\n".join(component.render() for component in self.css_components)


def main():
    builder = CodeBuilder()
    builder.add_html("Hello, world!")
    builder.add_css("color: blue;")
    html_code = builder.build_html()
    css_code = builder.build_css()

    print("Generated HTML:")
    print(html_code)
    print("\nGenerated CSS:")
    print(css_code)


if __name__ == "__main__":
    main()
```