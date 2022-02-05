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

        self.coin = arcade.Sprite("Assets/coin.png")
        self.coin.set_position(randint(self.coin.width/2, self.width - self.coin.height/2), randint(self.coin.width/2, self.height - self.coin.height/2))

        self.picked = 0
        self.max_Coins = 0

        self.time_Left = 10


    def on_update(self, delta_time: float):
        self.time_Left -= delta_time
        self.checkCol()
        if self.time_Left <= 0:
            self.time_Left = 10
            if self.picked > self.max_Coins:
                self.max_Coins = self.picked
            self.picked = 0



    def checkCol(self):
        if self.player.collides_with_sprite(self.coin):
            self.picked += 1
            x = randint(self.coin.width/2, self.width - self.coin.height/2)
            y = randint(self.coin.width/2, self.height - self.coin.height/2)
            self.coin.set_position(x,y)   


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin.draw()

        arcade.draw_text(str(round(self.time_Left,2)) ,self.width/2,self.height * 0.95, arcade.color.WHITE, anchor_x="center")
        arcade.draw_text("Picked: " + str(self.picked) ,self.width/2,self.height * 0.90, arcade.color.WHITE, anchor_x="center")
        arcade.draw_text("Max: " + str(self.max_Coins) ,self.width/2,self.height * 0.85, arcade.color.WHITE, anchor_x="center")


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.set_position(x,y)


MyGame()

arcade.run()