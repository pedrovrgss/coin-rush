from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.window import *

class Coin(Sprite):
    def __init__(self, image_file, x, y, frames=1, active = True):
        super().__init__(image_file, frames)
        self.x = x
        self.y = y
        self.active = active

    def draw(self):
        if self.active == True:
            super().draw()
    
    