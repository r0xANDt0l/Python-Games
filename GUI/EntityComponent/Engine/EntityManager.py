from Engine.Entity import *

class EntityManager():
    def __init__(self, app) -> None:
        self.entities = []
        self.entitiesEraser = []
        self.application = app
        
    def firstUpdate(self):
        for entity in self.entities:
            if entity.active:
                entity.firstUpdate()

    def update(self):
        for entity in self.entities:
            if entity.active:
                entity.update()
        self.checkCollisions()

    def lateUpdate(self):
        for entity in self.entities:
            if entity.active:
                entity.lateUpdate()

        for erase in self.entitiesEraser:
            self.entities.remove(erase)
        
        self.entitiesEraser.clear()

    def draw(self):
        for entity in self.entities:
            if entity.active:
                entity.draw()

    def checkCollisions(self):
        for entity in self.entities:
            eColl = entity.collider
            if eColl == None or not entity.active:
                continue
            for other in self.entities:
                otherColl = other.collider
                if otherColl == None or other == entity or not other.active:
                    continue
                if eColl.checkCollision(otherColl):
                    entity.onCollision(other)


    def addEntity(self, name:str = 'Entity') -> Entity:
        newEntity = Entity(self,name)
        self.entities.append(newEntity)
        return newEntity


    def removeEntity(self, entity: Entity):
        count = self.entities.count(entity) == 1
        if count == 1:
            self.entitiesEraser.append(entity)
        elif count == 0:
            print("No pude encontrar la entidad")
        elif count > 1:
            print("ERROR: Entidad duplicada en la lista", entity.name)
            self.application.exit()

        