import arcade
from arcade import key
from math import sqrt

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        # Say variables
        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/2, self.height/2)

        self.pixel_ratio = 100
        self.camPos = (0 , 0) #bird do be watching
        self.coin = arcade.Sprite("Assets/coin.png")
        self.coinPos = (3 , 0)

        self.speed = 5
        self.movement = {
            "up" :  False,
            "left" : False,
            "down" : False,
            "right" : False
        }

    def on_update(self, delta_time: float):
        #Save Position

        x, y = self.camPos

        #Change Position

        movX = self.movement["right"] - (self.speed * self.movement["left"])
        movY = self.movement["up"] - (self.speed * self.movement["down"])

        mod = sqrt(movX * movX + movY * movY) # Check module

        if mod != 0:
            movX = (movX/mod) * self.speed
            movY = (movY/mod) * self.speed
        
        x += ((self.speed * self.movement["right"]) - (self.speed * self.movement["left"])) * delta_time
        y += ((self.speed * self.movement["up"]) - (self.speed * self.movement["down"])) * delta_time

        #Return Position

        self.camPos = (x, y)
        



    def on_draw(self):
        arcade.start_render()
        coinPixelPoint = (self.width/2 + (self.coinPos[0] - self.camPos[0]) * self.pixel_ratio, 
                          self.height/2 + (self.coinPos[1] - self.camPos[1]) * self.pixel_ratio ) 
        self.coin.position = coinPixelPoint
        self.player.draw()
        self.coin.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.movement["up"] = True
        elif symbol == key.A:
            self.movement["left"] = True
        if symbol == key.S:
            self.movement["down"] = True
        elif symbol == key.D:
            self.movement["right"] = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.movement["up"] = False
        elif symbol == key.A:
            self.movement["left"] = False
        if symbol == key.S:
            self.movement["down"] = False
        elif symbol == key.D:
            self.movement["right"] = False

MyGame()

arcade.run()