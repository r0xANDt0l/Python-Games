from Components.Component import *

class ComponentPrint(Component):
    def __init__(self) -> None:
        super().__init__('ComponentPrint')
    
    def update(self):
        print(self.entity.transform.position)
