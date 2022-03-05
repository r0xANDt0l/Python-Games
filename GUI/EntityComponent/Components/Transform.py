from Components.Components import *
class transform():
    def __init__(self) -> None:
        self.position = (0,0)
        self.rotation = 0
        self.objScale = 1

    def translate(self, x : int = 0, y : int = 0):
        X, Y = self.position

        self.position = (x + X, y+ Y)

    def setPos(self, x : int, y : int):
        self.position = (x, y)


    def rotate(self, rotate: float):
        self.rotatation += rotate

    def setRotation(self, rotate: float):
        self.rotatation = rotate

    def scale(self, scl:float):
        self.objScale *= scl

    def setScale(self, scl:float):
        self.objScale = scl