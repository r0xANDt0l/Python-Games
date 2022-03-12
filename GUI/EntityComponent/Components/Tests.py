from Components.Component import *

class Tests(Component):
    def __init__(self) -> None:
        super().__init__('Tests')

    def update(self):
        if self.getInputManager().getKey(keyCode.SPACE):
            self.entity.transform.scale(1.01)