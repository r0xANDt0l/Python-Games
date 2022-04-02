from Engine.Components.Component import *

class Pruebas(Component):
    def __init__(self) -> None:
        super().__init__('Pruebas')

    def update(self):
        if self.getInputManager().getKeyDown(KeyCode.C):
            self.entity.transform.scale(0.5)
        if self.getInputManager().getKey(KeyCode.D):
            self.entity.transform.translate(1)
        if self.getInputManager().getKey(KeyCode.A):
            self.entity.transform.translate(-1)
        if self.getInputManager().getKey(KeyCode.W):
            self.entity.transform.translate(0,1)
        if self.getInputManager().getKey(KeyCode.S):
            self.entity.transform.translate(0,-1)


    def onCollisionEnter(self, other: Entity):
        otherPruebas = other.getComponent("Pruebas2")
        if otherPruebas != None:
            otherPruebas.randomPrint()

    def onCollisionExit(self, other: Entity):
        otherPruebas = other.getComponent("Pruebas2")
        if otherPruebas != None:
            otherPruebas.randomPrint()
