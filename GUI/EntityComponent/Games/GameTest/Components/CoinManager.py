from Engine.Components.Component import *
from Engine.Components.SpriteRenderer import SpriteRenderer
from Games.GameTest.Components.Coin import Coin

class CoinManager(Component):
    def __init__(self) -> None:
        super().__init__("CoinManager")

    def start(self):
        self.coins = [self.getEntityManager().addEntity("Coin"+ str(i)) for i in range(5)]
        for coin in self.coins:
            coin.addComponent(SpriteRenderer("GUI/EntityComponent/Games/GameTest/Assets/gold_1.png", 1, True, False))
            coin.addComponent(Coin())
        self.reset_game()

    def reset_game(self):
        for coin in self.coins:
            coin.getComponent("Coin").changePos()

        
        self.timer = 0