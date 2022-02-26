from gameObjects.gameObject import *

class coinObject(gameObject):
    def __init__(self, engine, imgPath:str) -> None:
        super().__init__(engine)
        self.coin = arcade.Sprite(imgPath)

    def draw(self):
        self.coin.draw()

    def setPos(self, x, y):
        super().setPos(x, y)
        self.coin.set_position(x,y)
        