import arcade
from arcade import key
from math import sqrt

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        # declare variables

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)

        self.speed = 200
        self.gravity = self.player.height * -5.5
        self.movement = {
            "jump" :  False,
            "left" : False,
            "right" : False
        }

    def on_update(self, delta_time: float):
        #Save Position

        x, y = self.player.position

        #Change Position

        movX = self.movement["right"] - (self.speed * self.movement["left"])
        movY = 0

        mod = sqrt(movX * movX + movY * movY) # Check module

        if mod != 0:
            movX = (movX/mod) * self.speed
            movY = (movY/mod) * self.speed
        
        x += movX * delta_time
        y += movY * delta_time

        # Check if it's inbounds

        if x > self.width - self.player.width/2:
            x = self.width - self.player.width/2  # Right side

        elif x < 0 + self.player.width/2:
            x = 0 + self.player.width/2  # Left side

        if y > self.height - self.player.height/2:
            y = self.height - self.player.height/2 # Top side

        elif y < 0 + self.player.height/2 :
            y = 0 + self.player.height/2 # Bottom side

        #Return Position

        self.player.set_position(x, y)
        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        

    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.movement["jump"] = True
        elif symbol == key.A:
            self.movement["left"] = True
        elif symbol == key.D:
            self.movement["right"] = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.movement["jump"] = False
        if symbol == key.A:
            self.movement["left"] = False
        if symbol == key.D:
            self.movement["right"] = False

MyGame()

arcade.run()