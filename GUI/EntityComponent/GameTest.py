from App import *
from Components.SprRender import SpriteRenderer
class gameTest(App):
    def __init__(self):
        super().__init__(800, 600, "GameTest")

        player = self.entityManager.addEntity("Player")
        player.addComp(componentPrint())

        self.run()


gameTest()