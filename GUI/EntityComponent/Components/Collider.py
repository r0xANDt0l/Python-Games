from __future__ import annotations
from Components.Component import *

class Collider(Component):
    def __init__(self, name : str) -> None:
        super().__init__("Collider")
        pass

    def checkCollision(self, other : Collider) -> bool:
        pass