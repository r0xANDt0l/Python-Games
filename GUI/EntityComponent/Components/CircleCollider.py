from __future__ import annotations
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

        if other.name == "circleCollider":
            pass