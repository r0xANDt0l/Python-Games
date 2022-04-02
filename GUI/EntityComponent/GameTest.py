from Application import *
from Components.Pruebas import Pruebas
from Components.SpriteRenderer import SpriteRenderer

class GameTest(Application):
    def __init__(self):
        super().__init__(800, 600, 'Pacooooo')

        player = self.entityManager.addEntity("Player")
        player.addComponent(SpriteRenderer("Assets/player.png"))
        player.addComponent(Pruebas())


        other = self.entityManager.addEntity("Other")
        other.addComponent(SpriteRenderer("Assets/player.png"))
        other.transform.setPosition(600, self.height/2)

        self.run()






GameTest()