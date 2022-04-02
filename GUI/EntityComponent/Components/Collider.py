from __future__ import annotations
from Components.Component import *

class Collider(Component):
    def __init__(self, name : str, debug = False) -> None:
        super().__init__(name)
        self.debug = debug
        self.debugSprite = None

    def checkCollision(self, other: Collider) -> bool:
        pass

    def draw(self):
        if self.debug:
            self.debugSprite.position = self.entity.transform.position
            self.debugSprite.draw()