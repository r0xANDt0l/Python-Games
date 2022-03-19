from Components.Component import *

class Pruebas(Component):
    def __init__(self) -> None:
        super().__init__('Pruebas')

    def update(self):
        if self.getInputManager().getKey(KeyCode.SPACE):
            self.entity.transform.translate(1, 0)