from Components.Transform import Transform

class Entity():
    def __init__(self, entityManager, name :str = 'Entity') -> None:
        self.name = name
        self.transform = Transform()
        self.components = []
        self.entityManager = entityManager

    def update(self):
        for component in self.components:
            component.update()

    def draw(self):
        for component in self.components:
            component.draw()

    def addComponent(self, component):
        self.components.append(component)
        component.setEntity(self)
        component.start()
