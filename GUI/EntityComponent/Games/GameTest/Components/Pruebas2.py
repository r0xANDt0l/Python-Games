from random import randint
from Engine.Components.Component import *

class Pruebas2(Component):
    def __init__(self) -> None:
        super().__init__('Pruebas2')
        self.randomPrint()

    def update(self):
        print(self.pr)
        if self.getInputManager().getKeyDown(KeyCode.T):
            self.entity.transform.scale(2)
        if self.getInputManager().getKeyDown(KeyCode.Y):
            self.entity.transform.scale(0.5)

    def randomPrint(self):
        self.pr = randint(0,100)