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
