from Components.Transform import transform
from Components.Components import *
class entity():
    def __init__(self, name: str = "Entity") -> None:
        self.name = name
        self.transform = transform()
        self.components = []

    def update(self):
        for component in self.entities:
            component.update()

    def draw(self):
        for component in self.entities:
            component.draw()

    def addComp(self, Component):
        self.components.append(Component)
        component.setEntity