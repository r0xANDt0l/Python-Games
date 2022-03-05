
from Components.Components import *
class componentPrint(component):
    def __init__(self) -> None:
        super().__init__("CompPrint")

    def update(self):
        print("Tienes 50 actualizaciones")
    