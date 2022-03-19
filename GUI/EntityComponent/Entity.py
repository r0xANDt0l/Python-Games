from Components.Transform import Transform

class Entity():
    def __init__(self, entityManager, name :str = 'Entity') -> None:
        self.name = name
        self.transform = Transform()
        self.components = []
        self.componentsD = {}
        self.entityManager = entityManager

    def update(self):
        for component in self.components:
            component.update()

    def draw(self):
        for component in self.components:
            component.draw()

    def addComponent(self, component):
        self.components.append(component)
        self.componentsD[component.name] = component
        component.setEntity(self)
        component.start()

    def getComponent(self, cName):
        if cName in self.componentsD:
            return self.componentsD[cName]
        return None