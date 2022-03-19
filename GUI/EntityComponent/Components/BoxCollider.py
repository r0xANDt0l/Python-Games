from math import sqrt
from Components.Collider import Collider
from Components.Component import *


class BoxCollider(Collider):
    def __init__(self, width: int = 50, height: int = 50) -> None:
        super().__init__("BoxCollider")
        self.width = width
        self.height = height
        self.originalWidth = width
        self.originalHeight = height

    def update(self):
        s = self.entity.transform.localScale
        self.width = self.originalWidth * s
        self.height = self.originalHeight * s

    def checkCollision(self, other: Collider) -> bool:

        posOther = other.entity.transform.position[:]
        posThis = self.entity.transform.position[:]

        if other.name == "CircleCollider":
            x = abs(posOther[0] - posThis[0])
            y = abs(posOther[1] - posThis[1])

            if x > (self.width/2 + other.rad) or y > (self.height/2 + other.rad): 
                return False 

            if x <= (self.width/2) or y <= (self.height/2): 
                return True 

            cornerDistance_sq = (x - self.width/2)**2 + (y - self.height/2)**2

            return cornerDistance_sq <= (other.rad**2)

        elif other.name == "BoxCollider":
            if posThis[0] < posOther[0] + other.width and posThis[0] + self.width > posOther[0] and posThis[1] < posOther[1] + other.height and posThis[1] + self.height > posOther[1]:
                return True
        return False
