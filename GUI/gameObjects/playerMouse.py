from gameObjects.gameObject import *

class playerMouse(gameObject):
    def __init__(self, engine, imgPath:str) -> None:
        super().__init__(engine)
        self.player = arcade.Sprite(imgPath)

    def draw(self):
        self.player.draw()

    def mouseMovement(self, x: float, y: float, dx: float, dy: float):
        self.setPos(x,y)

    def setPos(self, x, y):
        super().setPos(x, y)
        self.player.set_position(x,y)
        