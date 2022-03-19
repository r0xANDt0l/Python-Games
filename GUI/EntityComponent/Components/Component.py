from __future__ import annotations
import arcade
from Entity import *
from Application import *

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

    def getName(self)-> str:
        return self.name

    def getEntityManager(self) -> EntityManager:
        return self.entity.entityManager

    def getApplication(self) -> Application:
        return self.getEntityManager().application

    def getInputManager(self) -> InputManager:
        return self.getApplication().inputManager

    def setEntity(self, entity: Entity):
        self.entity = entity

    def getComponent(self, cName: str) -> Component:
        return self.entity.getComponent(cName)