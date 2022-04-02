import arcade
from EntityManager import EntityManager
from InputManager import *


class Application(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Application'):
        super().__init__(width, height, title)
        self.entityManager = EntityManager(self)
        self.inputManager = InputManager()

    def update(self, deltaTime: float):
        self.entityManager.update()
        self.inputManager.clearKeys()

    def on_draw(self):
        # Esto siempre es lo primero
        arcade.start_render()
        # Todo lo otro después
        self.entityManager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.inputManager.keyPressed(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        self.inputManager.keyReleased(symbol)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass

    def run(self):
        arcade.run()

    def exit(self):
        arcade.close_window()