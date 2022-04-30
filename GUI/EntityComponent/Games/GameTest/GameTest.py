from Engine.Application import *
from Games.GameTest.Scenes.PauseMenu import *
from Games.GameTest.Scenes.MainLevel import *


class GameTest(Application):
    def __init__(self):
        super().__init__(800, 600, 'GameTest', arcade.color.BABY_BLUE)

        self.sceneManager.addScene(MainLevel(self))
        self.sceneManager.addScene(PauseMenu(self))

        self.run()