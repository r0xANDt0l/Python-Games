import arcade
from arcade import key
from math import sqrt

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        # Say variables
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
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            print("Estas dando a la W")
        elif symbol == key.A:
            print("Estas dando a la A")
        if symbol == key.S:
            print("Estas dando a la S")
        elif symbol == key.D:
            print("Estas dando a la D")
        if symbol == key.SPACE:
            print("Estas saltando")

MyGame()

arcade.run()