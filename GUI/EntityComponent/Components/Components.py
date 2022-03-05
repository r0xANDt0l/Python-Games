from Entity import entity
class component():
    def __init__(self, name: str = "Component") -> None:
        self.name = name
        self.entity = None

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def getName(self) -> str:
        return self.name

    def setEntity(self, entity: entity):
        self.entity = entity