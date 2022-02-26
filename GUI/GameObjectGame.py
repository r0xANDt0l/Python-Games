from xmlrpc.client import MAXINT
import arcade

from gameObjects.playerMouse import *
from gameObjects.coinObject import *
from gameObjects.coinMgr import *

class MyGame(arcade.Window):
    def __init__(self, width = 800, height = 600, windowName = "osu pero no osu") -> None:
        super().__init__(width, height, windowName)
        self.set_mouse_visible(False)
        self.gameObjectList = []
        manager = coinMgr(self, [coinObject(self, "Assets/coin.png") for i in range( 5 ) ], playerMouse(self, "Assets/player.png"))
        # self.gameObjectList.append(manager)
        for coin in manager.coins:
            self.gameObjectList.append(coin)
        self.gameObjectList.append(manager.player)

        self.minTime = MAXINT

    def on_update(self, delta_time: float):
        for g in self.gameObjectList:
            g.update(delta_time)

    def on_draw(self):
        arcade.start_render()

        for g in self.gameObjectList:
            g.draw()


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for g in self.gameObjectList:
            g.mouseMovement(x,y,dx,dy)


MyGame()

arcade.run()