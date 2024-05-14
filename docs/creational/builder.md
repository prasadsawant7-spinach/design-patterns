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

## Another Example
``` py linenums="1" title="src/creational/builder_example.py"
from typing import List, Union


# Product classes
class Button:
    """A class representing a button UI component."""

    def __init__(self, text: str):
        """Initialize the Button with text."""
        self.text = text

    def display(self) -> None:
        """Display the button."""
        print(f"Button: {self.text}")


class TextField:
    """A class representing a text field UI component."""

    def __init__(self, label: str):
        """Initialize the TextField with a label."""
        self.label = label

    def display(self) -> None:
        """Display the text field."""
        print(f"Text Field: {self.label}")


class Checkbox:
    """A class representing a checkbox UI component."""

    def __init__(self, label: str):
        """Initialize the Checkbox with a label."""
        self.label = label

    def display(self) -> None:
        """Display the checkbox."""
        print(f"Checkbox: {self.label}")


# Builder interface
class DesignTool:
    """An interface for building UI components."""

    def create_button(self, text: str) -> None:
        """Create a button UI component."""
        pass

    def create_text_field(self, label: str) -> None:
        """Create a text field UI component."""
        pass

    def create_checkbox(self, label: str) -> None:
        """Create a checkbox UI component."""
        pass


# Concrete builder
class Figma(DesignTool):
    """A concrete builder for building simple UI components."""

    def __init__(self):
        """Initialize Figma."""
        self.components: List[Union[Button, TextField, Checkbox]] = []

    def create_button(self, text: str) -> None:
        """Create a button UI component."""
        self.components.append(Button(text))

    def create_text_field(self, label: str) -> None:
        """Create a text field UI component."""
        self.components.append(TextField(label))

    def create_checkbox(self, label: str) -> None:
        """Create a checkbox UI component."""
        self.components.append(Checkbox(label))

    def render_design(self) -> List[Union[Button, TextField, Checkbox]]:
        """Get the result of the design process."""
        return self.components


# Director
class Designer:
    """A class responsible for managing the construction process."""

    def __init__(self, designTool: DesignTool):
        """Initialize the Designer with a designTool."""
        self.designTool = designTool

    def build_basic_ui(self) -> None:
        """Build a basic UI."""
        self.designTool.create_button("Submit")
        self.designTool.create_text_field("Username")
        self.designTool.create_text_field("Password")
        self.designTool.create_checkbox("Remember me")


def main() -> None:
    """
    **Steps to implement:**
    **1. Instantiate Figma**
    **2. Instantiate Designer with the figma**
    **3. Designer builds a basic UI**
    **4. Get the constructed UI components**
    **5. Display the created UI components**
    """
    figma = Figma()
    designer = Designer(figma)
    designer.build_basic_ui()
    ui_components = figma.render_design()

    print("Created UI Components:")
    for component in ui_components:
        component.display()


if __name__ == "__main__":
    main()
```

## Class Diagram
``` mermaid
classDiagram
    class Button {
        display()
    }
    class TextField {
        display()
    }
    class Checkbox {
        display()
    }
    class DesignTool {
        create_button()
        create_text_field()
        create_checkbox()
    }
    class Figma {
        create_button()
        create_text_field()
        create_checkbox()
        render_design()
    }
    class Designer {
        build_basic_ui()
    }
    class UI {
        TextField
        Checkbox
        Button
    }
    Button <|-- Figma
    TextField <|-- Figma
    Checkbox <|-- Figma
    DesignTool --|> Figma
    DesignTool <|-- Designer
    Button --|> UI
    TextField --|> UI 
    Checkbox --|> UI
```