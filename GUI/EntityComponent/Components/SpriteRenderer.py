from Components.Component import *

class SpriteRenderer(Component):
    def __init__(self, path : str, scale : int = 1) -> None:
        super().__init__('SpriteRenderer')
        self.localScale = scale
        self.sprite = arcade.Sprite(path, scale)

    def start(self):
        app = self.getApp()
        self.entity.transform.setPosition(app.width/2, app.height/2)

    def update(self):
        tr = self.entity.transform
        self.sprite.position = tr.position
        self.sprite.angle = tr.rotation
        self.sprite.scale = tr.localScale * self.localScale

    def draw(self):
        self.sprite.draw()        

    def scale(self, s:float):
        self.localScale *= s

    def setScale(self, s:float):
        self.localScale = s