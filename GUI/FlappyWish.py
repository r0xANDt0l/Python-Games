import arcade
from arcade import key
from math import sqrt

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        # declare variables

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/2, self.height/2)

        self.speed = 500
        self.gravity = -0.5

        self.velX = 0
        self.velY = 0
        self.jumpForce = 10

        self.jump = False

    def on_update(self, delta_time: float):
        #Save Position

        y = self.player.position[1]

        #Change Position

        if self.jump:
            self.velY = self.jumpForce
            self.jump = False

        

        self.velY += self.gravity

    
        # x += self.velX * delta_time
        y += self.velY

        # Check if it's inbounds
        if y < self.player.height/2 :
            y = self.player.height/2 # Bottom side

        #Return Position

        self.player.set_position(self.width/2, y)
        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        

    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.jump = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.jump = False

MyGame()

arcade.run()