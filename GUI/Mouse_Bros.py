from math import sqrt
import arcade

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        #Change Arcade attributes
        self.set_mouse_visible(False)
        # Say variables
        self.coin = arcade.Sprite("Assets/coin.png")
        self.coin.set_position(self.width/2,self.height/2)

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)
        

    def on_update(self, delta_time: float):
        self.checkCol()
        
    def checkCol(self):
        val = 0
        if self.player.collides_with_sprite(self.coin):
            val +=1
            print(val)

    def on_draw(self):
        arcade.start_render()
        self.coin.draw()
        self.player.draw()
        
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        print(dx, dy)
        self.player.set_position(x,y)


MyGame()

arcade.run()