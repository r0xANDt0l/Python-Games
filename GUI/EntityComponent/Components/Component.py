from Application import *
from Entity import *
import arcade

class Component():
    def __init__(self, name: str = "Component") -> None:
        self.name = name
        self.entity = None

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def getName(self) -> str:
        return self.name

    def getEM(self) -> EntityManager:
        return self.entity.entityManager

    def getApp(self) -> Application:
        return self.getEM().application

    def setEntity(self, entity: Entity):
        self.entity = entity