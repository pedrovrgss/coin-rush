from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.window import *

class Enemy(Sprite):
    def __init__(self, image_file, speed = 200, frames=1):
        super().__init__(image_file, frames)
        self.speed = speed