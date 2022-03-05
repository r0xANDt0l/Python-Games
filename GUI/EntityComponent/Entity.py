class entity():
    def __init__(self, name: str = "Entity") -> None:
        self.name = name
        self.components = []

    def update(self):
        for component in self.entities:
            component.update()

    def draw(self):
        for component in self.entities:
            component.draw()