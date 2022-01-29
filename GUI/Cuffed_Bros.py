import arcade

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)
        self.coin = arcade.Sprite("Assets/coin.png")
        self.coin.set_position(self.width/2,self.height/2)

        self.player = arcade.Sprite("Assets/player.png")
        self.player.set_position(self.width/4, self.height/2)

    def on_update(self, delta_time: float):
        #Guardar pos
        x, y = self.player.position
        #Modificar pos
        x += 1
        #Devolver pos
        self.player.set_position(x, y)
        pass

    def on_draw(self):
        arcade.start_render()
        self.coin.draw()
        self.player.draw()

MyGame()

arcade.run()