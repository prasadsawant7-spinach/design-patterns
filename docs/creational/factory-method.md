---
title: Creational Design Patterns
description: Creational design patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.
---

# Creational Design Patterns

::: src.creational
::: src.creational.factory

## Source Code
``` py linenums="1" title="src/creational/factory.py"
from abc import ABC, abstractmethod

class DesignTool(ABC):
    @abstractmethod
    def createDesign(self) -> None:
        pass


class Figma(DesignTool):
    def createDesign(self) -> None:
        return "creating a design using Figma!"


class AdobeXD(DesignTool):
    def createDesign(self) -> None:
        return "creating a design using AdobeXD!"


class Zeplin(DesignTool):
    def createDesign(self) -> None:
        return "creating a design using Zeplin!"


class DesignToolProvider(ABC):
    @abstractmethod
    def getDesignTool(self) -> DesignTool:
        pass


class FigmaProvider(DesignToolProvider):
    def getDesignTool(self) -> DesignTool:
        return Figma()


class AdobeXDProvider(DesignToolProvider):
    def getDesignTool(self) -> DesignTool:
        return AdobeXD()


class ZeplinProvider(DesignToolProvider):
    def getDesignTool(self) -> DesignTool:
        return Zeplin()


class Designer:
    _design_tool: DesignTool = None
    def __init__(self, designToolProvider: DesignToolProvider) -> None:
        self._design_tool = designToolProvider.getDesignTool()

    def createDesign(self) -> DesignTool:
        return self._design_tool.createDesign()


def main():
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
```