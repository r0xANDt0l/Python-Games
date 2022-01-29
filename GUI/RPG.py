from unicodedata import name
import arcade

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "Ventana") -> None:
        super().__init__(width, height, windowName)


    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        pass

arcade.Window

arcade.open_window