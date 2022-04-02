import arcade
from arcade import key
from math import radians, cos, sin

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        # declare variables

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)

        self.speed = 100

        self.velX = 0
        self.velY = 0
        self.maxVel = 600

        self.rotateSpeed = 0.5
        self.velRot = 0
        self.maxRot = 10

        self.drag = 0.95
        self.angDrag = 0.95
        self.space = False

        self.movement = {
            "left" : False,
            "right" : False,
            "foward" :  False,
            "back" : False
        }

    def on_update(self, delta_time: float):
        #Save Position

        x, y = self.player.position

        #Change Position

        self.velRot += (self.movement["left"] - self.movement["right"]) * self.rotateSpeed

        if abs(self.velRot) > self.maxRot:
            self.velRot = self.maxRot * (self.velRot / abs(self.velRot))

        self.player.angle += self.velRot


        velBool = self.movement["foward"] - self.movement["back"]
        self.velX += cos(radians(self.player.angle + 90)) * velBool * self.speed
        self.velY += sin(radians(self.player.angle + 90)) * velBool * self.speed

        if abs(self.velX) > self.maxVel:
            self.velX = self.maxVel * (self.velX / abs(self.velX))
        if abs(self.velY) > self.maxVel:
            self.velY = self.maxVel * (self.velY / abs(self.velY))
    
        x += self.velX * delta_time
        y += self.velY * delta_time

        # Check if it's inbounds

        if x > self.width + self.player.width/2: # Right side
            x = -self.player.width/2  

        elif x < -self.player.width/2: # Left side
            x = self.width + self.player.width/2   

        if y > self.height + self.player.height/2: # Top side
            y = -self.player.height/2 

        elif y < -self.player.height/2 : # Bottom side
            y = self.height + self.player.height/2 


        if not self.space:
            self.velRot *= self.angDrag
            self.velX *= self.drag
            self.velY *= self.drag

        #Return Position

        self.player.set_position(x, y)
        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        

    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.movement["foward"] = True
        elif symbol == key.A:
            self.movement["left"] = True
        elif symbol == key.S:
            self.movement["back"] = True
        elif symbol == key.D:
            self.movement["right"] = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.W or symbol == key.SPACE:
            self.movement["foward"] = False
        if symbol == key.A:
            self.movement["left"] = False
        if symbol == key.D:
            self.movement["back"] = False
        if symbol == key.D:
            self.movement["right"] = False

MyGame()

arcade.run()