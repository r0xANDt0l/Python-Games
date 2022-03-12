from Application import *
from Components.Tests import Tests
from Components.SpriteRenderer import SpriteRenderer
from Components.ComponentPrint import ComponentPrint

class GameTest(Application):
    def __init__(self):
        super().__init__(800, 600, 'GameTest')

        player = self.entityManager.addEntity("Player")
        player.addComponent(SpriteRenderer("Assets/player.png", 0.5))
        player.addComponent(Tests())

        other = self.entityManager.addEntity("other")
        other.addComponent(SpriteRenderer("Assets/player.png", 0.5))
        other.transform.setPosition(600, self.height/2)

        self.run()






GameTest()