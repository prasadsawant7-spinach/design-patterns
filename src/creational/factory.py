# creational/factory.py

"""
**2. Factory Method**\n
The Factory Method Design Pattern is a creational design pattern used in software engineering to provide an interface for creating objects in a superclass, while allowing subclasses to alter the type of objects that will be created.
"""

from abc import ABC, abstractmethod


class DesignTool(ABC):
    """Abstract base class for design tools."""

    @abstractmethod
    def createDesign(self) -> None:
        """Creates a design using the respective design tool."""
        pass


class Figma(DesignTool):
    """Concrete implementation of the DesignTool interface for Figma."""

    def createDesign(self) -> None:
        """Creates a design using Figma."""
        return "creating a design using Figma!"


class AdobeXD(DesignTool):
    """Concrete implementation of the DesignTool interface for AdobeXD."""

    def createDesign(self) -> None:
        """Creates a design using AdobeXD."""
        return "creating a design using AdobeXD!"


class Zeplin(DesignTool):
    """Concrete implementation of the DesignTool interface for Zeplin."""

    def createDesign(self) -> None:
        """Creates a design using Zeplin."""
        return "creating a design using Zeplin!"


class DesignToolProvider(ABC):
    """Abstract base class for design tool providers."""

    @abstractmethod
    def getDesignTool(self) -> DesignTool:
        """Returns an instance of a design tool."""
        pass


class FigmaProvider(DesignToolProvider):
    """Concrete implementation of the DesignToolProvider interface for Figma."""

    def getDesignTool(self) -> DesignTool:
        """Returns an instance of Figma."""
        return Figma()


class AdobeXDProvider(DesignToolProvider):
    """Concrete implementation of the DesignToolProvider interface for AdobeXD."""

    def getDesignTool(self) -> DesignTool:
        """Returns an instance of AdobeXD."""
        return AdobeXD()


class ZeplinProvider(DesignToolProvider):
    """Concrete implementation of the DesignToolProvider interface for Zeplin."""

    def getDesignTool(self) -> DesignTool:
        """Returns an instance of Zeplin."""
        return Zeplin()


class Designer:
    """Class representing a designer who creates designs using a specific design tool."""

    _design_tool: DesignTool = None

    def __init__(self, designToolProvider: DesignToolProvider) -> None:
        """
        Initializes a Designer object with the provided design tool provider.

        Args:
            designToolProvider (DesignToolProvider): A provider of design tools.
        """
        self._design_tool = designToolProvider.getDesignTool()

    def createDesign(self) -> DesignTool:
        """
        Creates a design using the selected design tool.

        Returns:
            DesignTool: The design tool used to create the design.
        """
        return self._design_tool.createDesign()


def main():
    """
    **Steps to implement:**\n
    **1. Create Provider's Instance**\n
    **2. Create a Designer Instance by providing Provider's instance**\n
    **3. Call the method using Designer's Instance**\n
    """
    figma_provider = FigmaProvider()
    designer1 = Designer(figma_provider)
    print(f"Designer 1 {designer1.createDesign()}")

    adobeXD_provider = AdobeXDProvider()
    designer2 = Designer(adobeXD_provider)
    print(f"Designer 2 {designer2.createDesign()}")

    sketch_provider = ZeplinProvider()
    designer3 = Designer(sketch_provider)
    print(f"Designer 3 {designer3.createDesign()}")


if __name__ == "__main__":
    main()
