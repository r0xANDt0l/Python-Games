from xmlrpc.client import MAXINT
from Engine.Components.Component import *
from Engine.Components.SpriteRenderer import SpriteRenderer
from Engine.Components.Stopwatch import StopWatch
from GUI.EntityComponent.Engine.Components.AudioSource import AudioSource
from Games.GameTest.Components.Coin import Coin

class CoinManager(Component):
    def __init__(self, numCoins:int = 10) -> None:
        super().__init__("CoinManager")
        self.numCoins = numCoins
        self.picked = 0
        self.crono = StopWatch()
        self.bestTime = MAXINT

    def start(self):
        self.coins = [self.getEntityManager().addEntity("Coin"+ str(i)) for i in range(self.numCoins)]
        for coin in self.coins:
            coin.addComponent(SpriteRenderer("GUI/EntityComponent/Games/GameTest/Assets/gold_1.png", 0.5))
            coin.addComponent(AudioSource("GUI/EntityComponent/Games/GameTest/Assets/gold_1.png", 50))
            coin.addComponent(Coin(self))
        self.reset_game()

    def reset_game(self):
        for coin in self.coins:
            coin.active = True
            coin.getComponent("Coin").changePos()
        self.crono.start()


    def endRound(self):
        self.picked = 0
        if self.bestTime > self.crono.currentTime():
            self.bestTime = self.crono.currentTime()
        self.reset_game()

    def draw(self):
        arcade.draw_text(str(round(self.crono.currentTime(),2)) ,self.getApplication().width/2,self.getApplication().height * 0.95, arcade.color.WHITE, anchor_x="center")
        arcade.draw_text( "Min:" + str(round(self.bestTime,2))if self.bestTime != MAXINT else "Na", self.getApplication().width/2, self.getApplication().height* 0.9, arcade.color.WHITE, 20, anchor_x="center")

    def collectCoin(self, coin: Entity):
        if not coin.active:
            return

        if coin in self.coins:
            coin.active = False
            self.picked += 1
            if self.picked == self.numCoins:
                self.endRound()
