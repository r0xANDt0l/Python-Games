from tabnanny import check
from turtle import width
import arcade
from arcade import check_for_collision, key

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        self.coin = arcade.Sprite("Assets/coin.png")
        self.coin.set_position(self.width/2,self.height/2)

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)

        self.speed = 200
        self.movement = {
            "up" :  False,
            "left" : False,
            "down" : False,
            "right" : False
        }

    def on_update(self, delta_time: float):
        #Save Position

        x, y = self.player.position

        #Change Position
        
        x += ((self.speed * self.movement["right"]) - (self.speed*self.movement["left"])) * delta_time
        y += ((self.speed * self.movement["up"]) - (self.speed*self.movement["down"])) * delta_time

        # Check if it's inbounds

        if x > self.width - self.player.width/2:
            x = self.width - self.player.width/2  # Right side

        elif x < 0 + self.player.width/2:
            x = 0 + self.player.width/2  # Left side

        elif y > self.height - self.player.height/2:
            y = self.height - self.player.height/2 # Top side

        elif y < 0 + self.player.height/2 :
            y = 0 + self.player.height/2 # Bottom side

        #Return Position

        self.player.set_position(x, y)
        


    def checkCol(self):
        val = 0
        if self.player.collides_with_sprite(self.coin):
            val +=1
            print(val)

    def on_draw(self):
        arcade.start_render()
        self.coin.draw()
        self.player.draw()
        self.checkCol()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.movement["up"] = True
        elif symbol == key.A:
            self.movement["left"] = True
        elif symbol == key.S:
            self.movement["down"] = True
        elif symbol == key.D:
            self.movement["right"] = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.movement["up"] = False
        elif symbol == key.A:
            self.movement["left"] = False
        elif symbol == key.S:
            self.movement["down"] = False
        elif symbol == key.D:
            self.movement["right"] = False

MyGame()

arcade.run()