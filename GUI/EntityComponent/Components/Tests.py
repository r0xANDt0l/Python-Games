from Components.Component import *

class Tests(Component):
    def __init__(self) -> None:
        super().__init__('Tests')

    def update(self):
        self.entity.transform.scale(1.0001)