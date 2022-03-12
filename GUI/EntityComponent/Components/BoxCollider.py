from __future__ import annotations
from math import sqrt
from Components.Collider import *
from Components.Component import *

class boxCollider(Collider):
    def __init__(self, width : int = 50, height : int = 50) -> None:
        super().__init__("boxCollider")
        self.width = width
        self.height = height
        self.originalwidth = width
        self.originalheight = height

    def update(self):
        tr = self.entity.transform.localScale
        self.width = self.originalwidth * tr
        self.height = self.originalheight * tr

    def checkCollision(self, other : Collider) -> bool:

        posOther = other.entity.transform.position[:]
        posThis = self.entity.transform.position[:]

        if other.name == "circleCollider":
            pass
        elif other.name == "boxCollider":
            pass

        return False