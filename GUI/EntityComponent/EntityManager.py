from Entity import entity

class EntityManager():
    def __init__(self, app) -> None:
        self.entities = []
        self.application = app

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        for entity in self.entities:
            entity.draw()

    def addEntity(self, name : str = "entity") -> entity:
        newEntity = entity(name)
        self.entities.append(newEntity )

        return newEntity

