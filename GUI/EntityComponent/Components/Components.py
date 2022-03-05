class component():
    def __init__(self, name: str = "Component") -> None:
        self.name = name

    def update(self):
        pass

    def draw(self):
        pass

    def getName(self) -> str:
        return self.name