from Engine.Application import *
from Engine.Components.SpriteRenderer import SpriteRenderer

class Hexadash(Application):
    def __init__(self):
        super().__init__(800, 600, 'GameTest', arcade.color.BABY_BLUE)
        player = self.entityManager.addEntity("Player")
        player.addComponent(SpriteRenderer("GUI/EntityComponent/Games/Hexadash/Assets/Hexa.png"))

        self.run()