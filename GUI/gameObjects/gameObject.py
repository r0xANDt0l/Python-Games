import arcade

class gameObject():
    def __init__(self, engine: arcade.Window) -> None:
        self.engine = engine
        self.position = [0,0]

    def update(self, delta_time):
        pass

    def draw(self):
        pass

    def mouseMovement(self, x: float, y: float, dx: float, dy: float):
        pass
        
    def setPos(self, x, y):
        self.position = [x,y]

