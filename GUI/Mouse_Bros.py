from xmlrpc.client import MAXINT
import arcade
from random import randint

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        #Change Arcade attributes
        self.set_mouse_visible(False)
        # Say variables
        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)

        self.coins = [arcade.Sprite("Assets/coin.png") for i in range(5)]

        for coin in self.coins:
            x = randint(coin.width/2, width - coin.height/2)
            y = randint(coin.width/2, height - coin.height/2)
            coin.set_position(x,y)    

        self.timer = 0
        self.minTime = MAXINT


    def on_update(self, delta_time: float):
        self.timer += delta_time
        print(self.timer)
        if self.checkCol():
            print("Has acabao illo")

        if self.timer < self.minTime:
            self.minTime = self.timer


    def checkCol(self) -> bool:
        EraseQ = []
        for i in range(len(self.coins)):
            if self.player.collides_with_sprite(self.coins[i]):
                EraseQ.append(self.coins[i])

        for erase in EraseQ:
            self.coins.remove(erase)

        return not bool(len(self.coins))

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        for i in range(len(self.coins)):
            self.coins[i].draw()


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.set_position(x,y)


MyGame()

arcade.run()