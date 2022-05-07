from Engine.Scene import *
from Games.GameTest.Components.CoinDetector import CoinDetector
from Games.GameTest.Components.CoinManager import CoinManager
from Games.GameTest.Components.InfiniteScreen import InfiniteScreen
from Games.GameTest.Components.MovementDrag import MovementDrag
from Engine.Components.SpriteRenderer import SpriteRenderer


class MainLevel(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "MainLevel")

    def start(self):
        super().start()
        player = self.entityManager.addEntity("Player")
        player.addComponent(SpriteRenderer("GUI/EntityComponent/Games/GameTest/Assets/player_front.png"))
        player.addComponent(MovementDrag())
        player.addComponent(InfiniteScreen())
        player.addComponent(CoinDetector())           

        coinManager = self.entityManager.addEntity("CoinManager")
        coinManager.addComponent(CoinManager())