# creational/builder.py

"""
**1. Builder**\n
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.\n
"""


class HTMLComponent:
    """Represents a component of HTML code."""

    def __init__(self, content: str):
        """
        Initializes an HTMLComponent.

        Args:
            content (str): The content of the HTML component.
        """
        self.content = content

    def render(self) -> str:
        """
        Renders the HTML component.

        Returns:
            str: The HTML code representation of the component.
        """
        return f"<div>{self.content}</div>"


class CSSComponent:
    """Represents a component of CSS code."""

    def __init__(self, style: str):
        """
        Initializes a CSSComponent.

        Args:
            style (str): The CSS style of the component.
        """
        self.style = style

    def render(self) -> str:
        """
        Renders the CSS component.

        Returns:
            str: The CSS code representation of the component.
        """
        return f".element {{ {self.style} }}"


class CodeBuilder:
    """Builds HTML and CSS code by assembling components."""

    def __init__(self):
        """Initializes a CodeBuilder."""
        self.html_components = []
        self.css_components = []

    def add_html(self, content: str) -> 'CodeBuilder':
        """
        Adds an HTML component to the builder.

        Args:
            content (str): The content of the HTML component.

        Returns:
            CodeBuilder: The updated CodeBuilder instance.
        """
        self.html_components.append(HTMLComponent(content))
        return self

    def add_css(self, style: str) -> 'CodeBuilder':
        """
        Adds a CSS component to the builder.

        Args:
            style (str): The CSS style of the component.

        Returns:
            CodeBuilder: The updated CodeBuilder instance.
        """
        self.css_components.append(CSSComponent(style))
        return self

    def build_html(self) -> str:
        """
        Builds the HTML code from added HTML components.

        Returns:
            str: The generated HTML code.
        """
        return "\n".join(component.render() for component in self.html_components)

    def build_css(self) -> str:
        """
        Builds the CSS code from added CSS components.

        Returns:
            str: The generated CSS code.
        """
        return "\n".join(component.render() for component in self.css_components)


def main():
    """
    **Steps to implement:**\n
    **1. Create Code Builder's Instance**\n
    **2. Add HTML and CSS code**\n
    **3. Finally build the HTML & CSS code using Code Builder's Instance**\n
    """
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
