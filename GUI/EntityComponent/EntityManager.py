class EntityManager():
    def __init__(self) -> None:
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        for entity in self.entities:
            entity.draw()