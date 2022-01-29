import arcade
from arcade import key

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        self.coin = arcade.Sprite("Assets/coin.png")
        self.coin.set_position(self.width/2,self.height/2)

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)

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

        #Return Position
        self.player.set_position(x, y)
        pass

    def on_draw(self):
        arcade.start_render()
        self.coin.draw()
        self.player.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.movement["up"] = True
        elif symbol == key.A:
            self.movement["down"] = True
        elif symbol == key.S:
            self.movement["left"] = True
        elif symbol == key.D:
            self.movement["right"] = True

            
MyGame()

arcade.run()