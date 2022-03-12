from __future__ import annotations
from math import sqrt
from Components.Collider import *
from Components.Component import *

class circleCollider(Collider):
    def __init__(self, rad : int = 50) -> None:
        super().__init__("circleCollider")
        self.rad = rad
        self.originalRad = rad

    def update(self):
        self.rad = self.originalRad * self.entity.transform.localScale

    def checkCollision(self, other : Collider) -> bool:

        posOther = other.entity.transform.position[:]
        posThis = self.entity.transform.position[:]

        if other.name == "circleCollider":
            x = posOther[0] - posThis[0]
            y = posOther[1] - posThis[1]
            mod = sqrt(x**2 + y**2)
            if mod < self.rad + other.rad:
                return True
        elif other.name == "boxCollider":
            pass

        return False