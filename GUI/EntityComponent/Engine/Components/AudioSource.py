from Engine.Components.Component import *

class AudioSource(Component):
    def __init__(self, path: str, volume : int = 50, loop : bool = 0) -> None:
        super().__init__("AudioSource")
        self.audio = arcade.Sound(path)
        self.set_volume(volume)

    def audio_length(self):
        return self.audio.get_length()

    def get_length(self):
        return self.audio.get_length()

    def get_volume(self):
        return self.audio.get_volume() * 100
    
    def set_volume(self, volume : int):
        floatvolume = volume / 100
        self.audio.set_volume(floatvolume)
    
    def is_playing(self):
        return self.audio.is_playing()

    def is_complete(self):
        return self.audio.is_complete()

    def play(self, location : int = 0 , loop : bool = False):
        self.audio.play(self.get_volume(), location, loop)