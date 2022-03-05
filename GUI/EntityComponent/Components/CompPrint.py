from msilib.schema import Component
from unicodedata import name
from Components.Components import *
class componentPrint(Component):
    def __init__(self) -> None:
        super().__init__("CompPrint")

    def update(self):
        print("Tienes 50 actualizaciones pendientes")
    