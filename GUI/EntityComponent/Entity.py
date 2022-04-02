from msilib.schema import Component
from os import remove
from Components.Transform import Transform

class Entity():
    def __init__(self, entityManager, name :str = 'Entity') -> None:
        self.name = name
        self.transform = Transform()
        self.components = []
        self.componentsD = {}
        self.entityManager = entityManager
        self.collider = None


    def update(self):
        for component in self.components:
            component.update()

    def draw(self):
        for component in self.components:
            component.draw()

    def onCollision(self, other):
        for component in self.components:
            component.onCollision(other)

    def addComponent(self, component):
        name = component.name
        if self.getComponent(name) != None or (self.collider != None and (name == "BoxCollider" or name == "CircleCollider")):
            print("Ya existe un componente de tipo", name, "en", self.name)
            return
        self.components.append(component)
        self.componentsD[component.name] = component
        component.setEntity(self)
        component.start()

        if name == "BoxCollider" or name == "CircleCollider":
            self.collider = component

    def removeComponent(self, cName):
        component = self.getComponent(cName)
        if self.getComponent(cName) == None:
            print("La entidad", self.name,  "no tiene un componente de tipo", cName )
            return
        self.components.remove(component)
        self.componentsD[cName] = None
        if cName == "BoxCollider" or cName == "CircleCollider":
            self.collider = None


    def getComponent(self, cName):
        if cName in self.componentsD:
            return self.componentsD[cName]
        return None

    def getCollider(self):
        return self.collider