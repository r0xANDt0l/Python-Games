from arcade import key as KeyCode


class InputManager():
    def __init__(self) -> None:
        self.keys = {}

    def keyPressed(self, key: KeyCode):
        self.keys[key] = True

    def keyReleased(self, key : KeyCode):
        self.keys[key] = False

    def getKey(self, key : KeyCode):
        if key in self.keys:
            return self.keys[key]
        return False