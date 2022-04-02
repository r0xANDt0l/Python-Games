from Engine.Components.Component import *
from math import sin,cos,radians

class MovementDrag(Component):
    def __init__(self, space: bool = False) -> None:
        super().__init__('MovementDrag')
        self.speed = 100

        self.velX = 0
        self.velY = 0
        self.maxVel = 600

        self.rotateSpeed = 0.5
        self.velRot = 0
        self.maxRot = 10

        self.drag = 0.95
        self.angDrag = 0.95
        self.space = space

    def start(self):
        self.tr = self.entity.transform


    def update(self):
        
        up = self.getInputManager().getKey(KeyCode.W)
        left = self.getInputManager().getKey(KeyCode.A)
        down = self.getInputManager().getKey(KeyCode.S)
        right = self.getInputManager().getKey(KeyCode.D)

        self.velRot += (left - right) * self.rotateSpeed

        if abs(self.velRot) > self.maxRot:
            self.velRot = self.maxRot * (self.velRot / abs(self.velRot))

        self.tr.rotate(self.velRot)

        velBool = up - down
        self.velX += cos(radians(self.tr.rotation + 90)) * velBool * self.speed
        self.velY += sin(radians(self.tr.rotation + 90)) * velBool * self.speed

        if abs(self.velX) > self.maxVel:
            self.velX = self.maxVel * (self.velX / abs(self.velX))
        if abs(self.velY) > self.maxVel:
            self.velY = self.maxVel * (self.velY / abs(self.velY))
    
        x = self.velX * self.getApplication().deltaTime
        y = self.velY * self.getApplication().deltaTime

        #Return Position

        self.tr.translate(x,y)

        if not self.space:
            self.velRot *= self.angDrag
            self.velX *= self.drag
            self.velY *= self.drag