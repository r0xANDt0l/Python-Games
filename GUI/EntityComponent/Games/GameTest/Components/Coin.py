from random import randint
from Engine.Components.Component import *

class Coin(Component):
    def __init__(self, coinManager) -> None:
        super().__init__("Coin")
        self.coinManager = coinManager

    def start(self):
        self.tr = self.entity.transform
        self.sprite = self.getComponent("SpriteRenderer").sprite
        self.width = self.getApplication().width
        self.height = self.getApplication().height

    def changePos(self):
        x = randint(self.sprite.width / 2, self.width - self.sprite.width / 2)
        y = randint(self.sprite.height / 2, self.height - self.sprite.height / 2)
        self.tr.setPosition(x,y)

    def collect(self):
        self.coinManager.collectCoin(self.entity)