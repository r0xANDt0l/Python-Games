from gameObjects.gameObject import * 
from gameObjects.coinObject import coinObject
from gameObjects.playerMouse import playerMouse
from random import randint

class coinMgr(gameObject):
    def __init__(self, engine,  coinObject, playerMouse) -> None:
        super().__init__(engine)

        self.coins = coinObject
        self.player = playerMouse
        self.timer = 0
        self.minTime = 9999
        self.resetGame()

    
    def resetGame(self):
        for coin in self.coins:
            x = randint(0, self.engine.width)
            y = randint(0, self.engine.height)
            coin.setPos(x,y)   

        self.timer = 0

    def update(self, delta_time):
        self.timer += delta_time

        if self.checkCol():
            if self.timer < self.minTime:
                self.minTime = self.timer
            self.resetGame()

    def checkCol(self) -> bool:
        EraseQ = []
        for i in range(len(self.coins)):
            if self.player.collides_with_sprite(self.coins[i]):
                EraseQ.append(self.coins[i])

        for erase in EraseQ:
            self.coins.remove(erase)

        return not bool(len(self.coins))
    
    def draw(self):
        arcade.draw_text(str(round(self.timer,2)) ,self.width/2,self.height * 0.95, arcade.color.WHITE, anchor_x="center")
        arcade.draw_text("Min: " + str(round(self.minTime,2)) ,self.width/2,self.height * 0.85, arcade.color.WHITE, anchor_x="center")
