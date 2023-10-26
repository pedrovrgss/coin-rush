from PPlay.gameimage import *
from PPlay.sprite import *

class Area(Sprite):
    def __init__(self, image_file, frames=1, width = 200, height = 200):
        super().__init__(image_file, frames)
        self.width = width
        self.height = height
    
    def change_frame(self, frame):
        self.frame = frame
        self.img = self.frames[frame]

        