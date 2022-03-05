import arcade

from EntityManager import EntityManager

class App(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Arcade Window'):
        super().__init__(width, height, title)
        self.entityManager = EntityManager()

    def update(self, delta_time: float):
        self.entityManager.update()

    def on_draw(self):
        # Recuerda! El start_render siempre es lo primero.
        arcade.start_render()
        
        self.entityManager.draw

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass

    def run(self):
        arcade.run()

    def exit(self):
        arcade.close_window()