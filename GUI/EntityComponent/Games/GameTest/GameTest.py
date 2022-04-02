from GUI.EntityComponent.Engine.Application import *
from Games.GameTest.Components.Pruebas import Pruebas
from Games.GameTest.Components.Pruebas2 import Pruebas2
from Engine.Components.SpriteRenderer import SpriteRenderer

class GameTest(Application):
    def __init__(self):
        super().__init__(800, 600, 'GameTest')

        player = self.entityManager.addEntity("Player")
        player.addComponent(SpriteRenderer("Games/GameTest/Assets/player_front.png"))
        player.addComponent(Pruebas())                 

        other = self.entityManager.addEntity("Other")
        other.addComponent(SpriteRenderer("Games/GameTest/Assets/player_front.png"))
        other.addComponent(Pruebas2())
        other.transform.setPosition(600, self.height/2)

        self.run()