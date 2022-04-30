from Engine.Components.Component import *

class InfiniteScreen(Component):
    def __init__(self) -> None:
        super().__init__("InfiniteScreen")

    def start(self):
        self.tr = self.entity.transform
        self.sprite = self.getComponent("SpriteRenderer").sprite
        self.width = self.getApplication().width
        self.height = self.getApplication().height

    def update(self):
        if self.getInputManager().getKeyDown(KeyCode.ESCAPE):
            self.getSceneManager().pushScene(1)


        x, y = self.tr.position

        if x > self.width + self.sprite.width/2: # Right side
            x = -self.sprite.width/2  

        elif x < -self.sprite.width/2: # Left side
            x = self.width + self.sprite.width/2   

        if y > self.height + self.sprite.height/2: # Top side
            y = -self.sprite.height/2 

        elif y < -self.sprite.height/2 : # Bottom side
            y = self.height + self.sprite.height/2 

        self.tr.setPosition(x,y)
