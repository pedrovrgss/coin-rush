from PPlay.gameimage import *
from PPlay.animation import *
from PPlay.sprite import *

class Area(Sprite):
    def __init__(self, image_file, frames=1, width = 200, height = 200):
        super().__init__(image_file, frames)
        self.width = width
        self.height = height
    
    def change_frame(self, player):
        if player.collided(self):
            self.curr_frame = 1
        else:
            self.curr_frame = 0

        