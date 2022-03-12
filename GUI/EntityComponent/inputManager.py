from arcade import key as keyCode

class inputManager():
    def __init__(self) -> None:
        self.keys = {}
        
    def keyDown(self, key : keyCode):
        self.keys[key] = True

    def keyUp(self, key : keyCode):
        self.keys[key] = False

    def getKey(self, key : keyCode):
        if key in self.keys:
            return self.keys[key]
        return False