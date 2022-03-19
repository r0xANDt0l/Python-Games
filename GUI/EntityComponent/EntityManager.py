from Entity import Entity

class EntityManager():
    def __init__(self, app) -> None:
        self.entities = []
        self.application = app

    def update(self):
        for entity in self.entities:
            entity.update()
        self.checkCollisions()

    def checkCollisions(self):
        pass


    def draw(self):
        for entity in self.entities:
            entity.draw()

    def addEntity(self, name:str = 'Entity') -> Entity:
        newEntity = Entity(self,name)
        self.entities.append(newEntity)
        return newEntity