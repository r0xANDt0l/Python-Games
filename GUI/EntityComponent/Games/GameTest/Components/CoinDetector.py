from calendar import c
from Engine.Components.Component import *
from Engine.Components.SpriteRenderer import SpriteRenderer
from Games.GameTest.Components.Coin import Coin

class CoinDetector(Component):
    def __init__(self) -> None:
        super().__init__("Coin")


    def onCollisionEnter(self, other: Entity):

        c = other.getComponent("Coin")

        if c != None:
            c.collect()