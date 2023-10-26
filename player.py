from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.window import *
from area import Area


class Player(Sprite):
    def __init__(self, image_file, speed, frames=1, win = False):
        super().__init__(image_file, frames)
        self.speed = speed
        self.win = win
        
    def return_base(self, BASE_WIDTH, BASE_HEIGHT):
        self.x = BASE_WIDTH / 2 - self.width / 2
        self.y = BASE_HEIGHT / 2 - self.height / 2
    
    def win(self):
        self.win = True

class Enemy(Sprite):
    def __init__(self, image_file, speed, frames=1):
        super().__init__(image_file, frames)
        self.speed = speed
