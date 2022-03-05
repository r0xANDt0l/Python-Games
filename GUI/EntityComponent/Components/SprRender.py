import arcade
from Components.Components import *
class SpriteRenderer(component):
    def __init__(self, path) -> None:
        super().__init__("SpriteRenderer")
        self.sprite = arcade.Sprite(path)

    

    def draw(self):
        self.sprite.draw()