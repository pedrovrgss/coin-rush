from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from player import Player, Enemy
from area import Area

WINDOW = Window(1300, 800)
WINDOW.set_title("Coin Rush - Alpha 1.0.0")


KEYBOARD = Keyboard()

BASE = Area("assets/base.png", 2)
WIN_AREA = Area("assets/winarea.png", 2)
BASE.set_position(0, (WINDOW.height) - (BASE.height))
WIN_AREA.set_position(WINDOW.width - WIN_AREA.width, 0)


BOX= Sprite("assets/box.png", 2)
BOX.width = 400
BOX.height = 400


PLAYER = Player("assets/player.png", 250)
PLAYER.width = 15
PLAYER.height = 15
PLAYER.set_position(BASE.x + BASE.height / 2 - PLAYER.width / 2, BASE.y + BASE.width / 2 - PLAYER.height / 2)
SPEED_TOP = PLAYER.speed * WINDOW.delta_time()
SPEED_LEFT = PLAYER.speed * WINDOW.delta_time()
SPEED_RIGHT = PLAYER.speed * WINDOW.delta_time()
SPEED_BOTTOM = PLAYER.speed * WINDOW.delta_time()

ENEMY_01 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_01.set_position(WINDOW.width * 0.10, WINDOW.height * 0.05)
ENEMY_02 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_02.set_position(WINDOW.width * 0.10, WINDOW.height * 0.12)
ENEMY_03 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_03.set_position(WINDOW.width * 0.10, WINDOW.height * 0.19)

ENEMY_04 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_04.set_position(WINDOW.width * 0.25, WINDOW.height * 0.8)
ENEMY_05 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_05.set_position(WINDOW.width * 0.25, WINDOW.height * 0.87)
ENEMY_06 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_06.set_position(WINDOW.width * 0.25, WINDOW.height * 0.94)

ENEMY_07 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_07.set_position(WINDOW.width * 0.70, WINDOW.height * 0.3)
ENEMY_08 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_08.set_position(WINDOW.width * 0.76, WINDOW.height * 0.3)
ENEMY_09 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_09.set_position(WINDOW.width * 0.82, WINDOW.height * 0.3)
ENEMY_10 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_10.set_position(WINDOW.width * 0.88, WINDOW.height * 0.3)
ENEMY_11 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
ENEMY_11.set_position(WINDOW.width * 0.94, WINDOW.height * 0.3)

def DRAW_ENEMIES():
    ENEMY_01.draw()
    ENEMY_02.draw()
    ENEMY_03.draw()

    ENEMY_04.draw()
    ENEMY_05.draw()
    ENEMY_06.draw()

    ENEMY_07.draw()
    ENEMY_08.draw()
    ENEMY_09.draw()
    ENEMY_10.draw()
    ENEMY_11.draw()

def DRAW_BOX():
    BOX.set_position((WINDOW.width / 2) - (BOX.width / 2), (WINDOW.height / 2) - (BOX.height / 2))
    BOX.draw()

def MOVEMENT():
    if KEYBOARD.key_pressed("W"):
        PLAYER.y -= SPEED_TOP
    if KEYBOARD.key_pressed("S"):
        PLAYER.y += SPEED_BOTTOM
    if KEYBOARD.key_pressed("A"):
        PLAYER.x -= SPEED_LEFT
    if KEYBOARD.key_pressed("D"):
        PLAYER.x += SPEED_RIGHT

def SCREEN_BLOCK():
    if PLAYER.x < 0:
        PLAYER.x = 0
    if PLAYER.x > WINDOW.width - PLAYER.width:
        PLAYER.x = WINDOW.width - PLAYER.width
    if PLAYER.y < 0:
        PLAYER.y = 0
    if PLAYER.y > WINDOW.height - PLAYER.height:
        PLAYER.y = WINDOW.height - PLAYER.height

def CHECK_COLLISION():
    if KEYBOARD.key_pressed("A"):
        if (
            PLAYER.y > BOX.y and PLAYER.y < BOX.y + BOX.height - 1 and
            PLAYER.x > BOX.x and PLAYER.x - PLAYER.speed * WINDOW.delta_time() < BOX.x + BOX.width
        ):
            PLAYER.x = BOX.x + BOX.width
        else:
            PLAYER.x -= PLAYER.speed * WINDOW.delta_time()


    if KEYBOARD.key_pressed("D"):
        if (
            PLAYER.y > BOX.y and PLAYER.y < BOX.y + BOX.height - 1 and
            PLAYER.x + PLAYER.width < BOX.x + BOX.width and PLAYER.x + PLAYER.width + PLAYER.speed * WINDOW.delta_time() > BOX.x
        ):
            PLAYER.x = BOX.x - PLAYER.width
        else:
            PLAYER.x += PLAYER.speed * WINDOW.delta_time()


    if KEYBOARD.key_pressed("W"):
        if (
            PLAYER.x > BOX.x and PLAYER.x < BOX.x + BOX.width - 1 and
            PLAYER.y > BOX.y and PLAYER.y - PLAYER.speed * WINDOW.delta_time() < BOX.y + BOX.height
        ):
            PLAYER.y = BOX.y + BOX.height
        else:
            PLAYER.y -= PLAYER.speed * WINDOW.delta_time()


    if KEYBOARD.key_pressed("S"):
        if (
            PLAYER.x > BOX.x and PLAYER.x < BOX.x + BOX.width - 1 and
            PLAYER.y + PLAYER.height < BOX.y + BOX.height and PLAYER.y + PLAYER.height + PLAYER.speed * WINDOW.delta_time() > BOX.y
        ):
            PLAYER.y = BOX.y - PLAYER.height
        else:
            PLAYER.y += PLAYER.speed * WINDOW.delta_time()

while True:
    WIN_AREA.draw()

    BASE.draw()
        
    DRAW_BOX()

    DRAW_ENEMIES()

    PLAYER.draw()
    MOVEMENT()
    SCREEN_BLOCK()
    CHECK_COLLISION()


    WINDOW.update()
    WINDOW.set_background_color((199, 232, 243))