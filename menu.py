from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
from game import game

class Button(Sprite):
    def __init__(self, image_file, difficulty = 1, frames = 1):
        super().__init__(image_file, frames)
        self.width = self.width
        self.height = self.height
        self.difficulty = difficulty
        
    def clicked(self):
        MOUSE = Mouse()
        if MOUSE.is_over_object(self) and MOUSE.is_button_pressed(1):
            return True
        else:
            return False

def menu():
    WINDOW = Window(1300, 800)
    WINDOW.set_title("Coin Rush - Beta 2.0.1")
    KEYBOARD = Keyboard()

    play = Button("assets/play.png")
    play.set_position(100, 100)
    easy = Button("assets/easy.png", 1.0)
    easy.set_position(240, 150)
    medium = Button("assets/medium.png", 1.5)
    medium.set_position(240, 220)
    hard = Button("assets/hard.png", 2.0)
    hard.set_position(240, 290)

    
    while True:
        """
        TELA INICIAL
        """
        WINDOW.set_background_color((255, 248, 225))
        play.draw()
        WINDOW.update()


        """
        TELA DE DIFICULDADE
        """
        if play.clicked():
            while not KEYBOARD.key_pressed("ESC"):
                WINDOW.set_background_color((255, 248, 225))
                """
                ESCOLHA DE DIFICULDADE
                """
                easy.draw()
                if easy.clicked():
                    game(easy.difficulty, WINDOW, KEYBOARD)
                medium.draw()
                if medium.clicked():
                    game(medium.difficulty, WINDOW, KEYBOARD)
                hard.draw()
                if hard.clicked():
                    game(hard.difficulty, WINDOW, KEYBOARD)
                
                    
                play.draw()
                WINDOW.update()


menu()
