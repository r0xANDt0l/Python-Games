from __future__ import annotations
from Components.Collider import *
from Components.Component import *

class boxCollider(Collider):
    def __init__(self) -> None:
        super().__init__("boxCollider")
        pass

    def checkCollision(self, other : Collider) -> bool:
        pass