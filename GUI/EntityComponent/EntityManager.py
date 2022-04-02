from Entity import *

class EntityManager():
    def __init__(self, app) -> None:
        self.entities = []
        self.application = app

    def update(self):
        for entity in self.entities:
            entity.update()
        self.checkCollisions()

    def checkCollisions(self):
        for entity in self.entities:
            eColl = entity.collider
            if eColl == None:
                continue
            for other in self.entities:
                otherColl = other.collider
                if otherColl == None or other == entity:
                    continue
                if eColl.checkCollision(otherColl):
                    entity.onCollision(other)


    def draw(self):
        for entity in self.entities:
            entity.draw()

    def addEntity(self, name:str = 'Entity') -> Entity:
        newEntity = Entity(self,name)
        self.entities.append(newEntity)
        return newEntity