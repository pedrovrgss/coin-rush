from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from player import Player
from enemy import Enemy
from area import Area
from coin import Coin
"""""
    INPUT E TELA
"""""

def game(DIFICULDADE, WINDOW: Window, KEYBOARD: Keyboard):

    DIFICULDADE_ATUAL = DIFICULDADE


    """
        ÁREAS DO JOGO
    """

    BASE = Area("assets/base.png", 2)
    WIN_AREA = Area("assets/winarea.png", 2)
    BASE.set_position(0, (WINDOW.height) - (BASE.height))
    WIN_AREA.set_position(WINDOW.width - WIN_AREA.width, 0)

    BOX= Sprite("assets/box.png", 2)
    BOX.width = 400
    BOX.height = 400



    """
        OBJETOS DO JOGO
    """

    PLAYER = Player("assets/player.png", 200)
    PLAYER.width = 15
    PLAYER.height = 15
    PLAYER.set_position(BASE.x + BASE.height / 2 - PLAYER.width / 2, BASE.y + BASE.width / 2 - PLAYER.height / 2)
    SPEED_TOP = PLAYER.speed * WINDOW.delta_time()
    SPEED_LEFT = PLAYER.speed * WINDOW.delta_time()
    SPEED_RIGHT = PLAYER.speed * WINDOW.delta_time()
    SPEED_BOTTOM = PLAYER.speed * WINDOW.delta_time()


    """
    CRIAÇÃO DE INIMIGOS
    """

    ## BLOCO SUPERIOR

    ENEMY_01 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_01.set_position(WINDOW.width * 0.10, WINDOW.height * 0.05)
    DIRECTION_01 = 1

    ENEMY_02 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_02.set_position(WINDOW.width * 0.50, WINDOW.height * 0.12)
    DIRECTION_02 = 1

    ENEMY_03 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_03.set_position(WINDOW.width * 0.80, WINDOW.height * 0.19)
    DIRECTION_03 = -1


    ## BLOCO INFERIOR

    ENEMY_04 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_04.set_position(WINDOW.width * 0.25, WINDOW.height * 0.8)
    DIRECTION_04 = 1

    ENEMY_05 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_05.set_position(WINDOW.width * 0.60, WINDOW.height * 0.87)
    DIRECTION_05 = 1

    ENEMY_06 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_06.set_position(WINDOW.width * 0.95, WINDOW.height * 0.94)
    DIRECTION_06 = -1


    ## BLOCO DIREITO

    ENEMY_07 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_07.set_position(WINDOW.width * 0.70, WINDOW.height * 0.75)
    DIRECTION_07 = -1

    ENEMY_08 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_08.set_position(WINDOW.width * 0.76, WINDOW.height * 0.25)
    DIRECTION_08 = 1

    ENEMY_09 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_09.set_position(WINDOW.width * 0.82, WINDOW.height * 0.75)
    DIRECTION_09 = -1

    ENEMY_10 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_10.set_position(WINDOW.width * 0.88, WINDOW.height * 0.25)
    DIRECTION_10 = 1

    ENEMY_11 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_11.set_position(WINDOW.width * 0.94, WINDOW.height * 0.75)
    DIRECTION_11 = -1


    ## BLOCO ESQUERDO

    ENEMY_12 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_12.set_position(WINDOW.width * 0.01, WINDOW.height * 0.27)
    DIRECTION_12 = 1

    ENEMY_13 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_13.set_position(WINDOW.width * 0.06, WINDOW.height * 0.7)
    DIRECTION_13 = -1

    ENEMY_14 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_14.set_position(WINDOW.width * 0.11, WINDOW.height * 0.27)
    DIRECTION_14 = 1

    ENEMY_15 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_15.set_position(WINDOW.width * 0.16, WINDOW.height * 0.7)
    DIRECTION_15 = -1

    ENEMY_16 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_16.set_position(WINDOW.width * 0.21, WINDOW.height * 0.27)
    DIRECTION_16 = 1

    ENEMY_17 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_17.set_position(WINDOW.width * 0.26, WINDOW.height * 0.7)
    DIRECTION_17 = -1

    ENEMY_18 = Enemy("assets/enemy.png", 200 * WINDOW.delta_time())
    ENEMY_18.set_position(WINDOW.width * 0.31, WINDOW.height * 0.27)
    DIRECTION_18 = 1

    if DIFICULDADE == 1.0:
        BONUS_VEL = 0.5
    elif DIFICULDADE == 1.5:
        BONUS_VEL = 0.4
    else:
        BONUS_VEL = 0.3



    COIN_01 = Coin("assets/coin.png", WINDOW.width * 0.5, WINDOW.height * 0.05 + 6)
    COIN_02 = Coin("assets/coin.png", WINDOW.width * 0.5, WINDOW.height * 0.12 + 6)
    COIN_03 = Coin("assets/coin.png", WINDOW.width * 0.5, WINDOW.height * 0.19 + 6)

    COIN_04 = Coin("assets/coin.png", WINDOW.width * 0.6, WINDOW.height * 0.8 + 6)
    COIN_05 = Coin("assets/coin.png", WINDOW.width * 0.6, WINDOW.height * 0.87 + 6)
    COIN_06 = Coin("assets/coin.png", WINDOW.width * 0.6, WINDOW.height * 0.94 + 6)

    COIN_07 = Coin("assets/coin.png", WINDOW.width * 0.70 + 6, WINDOW.height * 0.5)
    COIN_08 = Coin("assets/coin.png", WINDOW.width * 0.76 + 6, WINDOW.height * 0.5)
    COIN_09 = Coin("assets/coin.png", WINDOW.width * 0.82 + 6, WINDOW.height * 0.5)
    COIN_10 = Coin("assets/coin.png", WINDOW.width * 0.88 + 6, WINDOW.height * 0.5)
    COIN_11 = Coin("assets/coin.png", WINDOW.width * 0.94 + 6, WINDOW.height * 0.5)

    COIN_12 = Coin("assets/coin.png", WINDOW.width * 0.01 + 6, WINDOW.height * 0.485)
    COIN_13 = Coin("assets/coin.png", WINDOW.width * 0.06 + 6, WINDOW.height * 0.485)
    COIN_14 = Coin("assets/coin.png", WINDOW.width * 0.11 + 6, WINDOW.height * 0.485)
    COIN_15 = Coin("assets/coin.png", WINDOW.width * 0.16 + 6, WINDOW.height * 0.485)
    COIN_16 = Coin("assets/coin.png", WINDOW.width * 0.21 + 6, WINDOW.height * 0.485)
    COIN_17 = Coin("assets/coin.png", WINDOW.width * 0.26 + 6, WINDOW.height * 0.485)
    COIN_18 = Coin("assets/coin.png", WINDOW.width * 0.31 + 6, WINDOW.height * 0.485)

    COINS = 0



    """
        FUNÇÕES DO JOGO
    """

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

        ENEMY_12.draw()
        ENEMY_13.draw()
        ENEMY_14.draw()
        ENEMY_15.draw()
        ENEMY_16.draw()
        ENEMY_17.draw()
        ENEMY_18.draw()

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

    DEATHS = 0
    def CHECK_DEATH(DEATHS):
        if PLAYER.collided(ENEMY_01) or PLAYER.collided(ENEMY_02) or PLAYER.collided(ENEMY_03) or PLAYER.collided(ENEMY_04) or PLAYER.collided(ENEMY_05) or PLAYER.collided(ENEMY_06) or PLAYER.collided(ENEMY_07) or PLAYER.collided(ENEMY_08) or PLAYER.collided(ENEMY_09) or PLAYER.collided(ENEMY_10) or PLAYER.collided(ENEMY_11) or PLAYER.collided(ENEMY_12) or PLAYER.collided(ENEMY_13) or PLAYER.collided(ENEMY_14) or PLAYER.collided(ENEMY_15) or PLAYER.collided(ENEMY_16) or PLAYER.collided(ENEMY_17) or PLAYER.collided(ENEMY_18):
            PLAYER.set_position(BASE.x + BASE.height / 2 - PLAYER.width / 2, BASE.y + BASE.width / 2 - PLAYER.height / 2)
            DEATHS += 1
        return DEATHS

    def DRAW_COINS():
        COIN_01.draw()
        COIN_02.draw()
        COIN_03.draw()
        COIN_04.draw()
        COIN_05.draw()
        COIN_06.draw()
        COIN_07.draw()
        COIN_08.draw()
        COIN_09.draw()
        COIN_10.draw()
        COIN_11.draw()
        COIN_12.draw()
        COIN_13.draw()
        COIN_14.draw()
        COIN_15.draw()
        COIN_16.draw()
        COIN_17.draw()
        COIN_18.draw()

    def CHECK_COIN(COINS):
        if PLAYER.collided(COIN_01) and COIN_01.active:
            COIN_01.active = False
            COINS += 1
        if PLAYER.collided(COIN_02) and COIN_02.active:
            COIN_02.active = False
            COINS += 1
        if PLAYER.collided(COIN_03) and COIN_03.active:
            COIN_03.active = False
            COINS += 1
        if PLAYER.collided(COIN_04) and COIN_04.active:
            COIN_04.active = False
            COINS += 1
        if PLAYER.collided(COIN_05) and COIN_05.active:
            COIN_05.active = False
            COINS += 1
        if PLAYER.collided(COIN_06) and COIN_06.active:
            COIN_06.active = False
            COINS += 1
        if PLAYER.collided(COIN_07) and COIN_07.active:
            COIN_07.active = False
            COINS += 1
        if PLAYER.collided(COIN_08) and COIN_08.active:
            COIN_08.active = False
            COINS += 1
        if PLAYER.collided(COIN_09) and COIN_09.active:
            COIN_09.active = False
            COINS += 1
        if PLAYER.collided(COIN_10) and COIN_10.active:
            COIN_10.active = False
            COINS += 1
        if PLAYER.collided(COIN_11) and COIN_11.active:
            COIN_11.active = False
            COINS += 1
        if PLAYER.collided(COIN_12) and COIN_12.active:
            COIN_12.active = False
            COINS += 1
        if PLAYER.collided(COIN_13) and COIN_13.active:
            COIN_13.active = False
            COINS += 1
        if PLAYER.collided(COIN_14) and COIN_14.active:
            COIN_14.active = False
            COINS += 1
        if PLAYER.collided(COIN_15) and COIN_15.active:
            COIN_15.active = False
            COINS += 1
        if PLAYER.collided(COIN_16) and COIN_16.active:
            COIN_16.active = False
            COINS += 1
        if PLAYER.collided(COIN_17) and COIN_17.active:
            COIN_17.active = False
            COINS += 1
        if PLAYER.collided(COIN_18) and COIN_18.active:
            COIN_18.active = False
            COINS += 1
        return COINS
        
    WIN = False

    """
        LOOP DO JOGO
    """

    while True:
        WIN_AREA.draw()
        WIN_AREA.change_frame(PLAYER)

        BASE.draw()
        BASE.change_frame(PLAYER)
            
        DRAW_BOX()

        DRAW_COINS()

        DRAW_ENEMIES()

        PLAYER.draw()
        MOVEMENT()
        SCREEN_BLOCK()
        CHECK_COLLISION()
        DEATHS = CHECK_DEATH(DEATHS)
        COINS = CHECK_COIN(COINS)
        
        WINDOW.draw_text("DEATHS:{}".format(DEATHS), 10, 10, 22, (230, 223, 0), "VCR OSD Mono")

        """
        MOVIMENTAÇÃO DOS INIMIGOS
        """
        ENEMIES_SPEED = 300 * DIFICULDADE * WINDOW.delta_time()


        ## BLOCO SUPERIOR

        ENEMY_01.move_x(ENEMIES_SPEED * DIRECTION_01)
        if ENEMY_01.x < WINDOW.width * 0.10 or ENEMY_01.x > WINDOW.width * 0.80:
            ENEMY_01.x -= 5*DIRECTION_01
            DIRECTION_01 *= -1

        ENEMY_02.move_x(ENEMIES_SPEED * DIRECTION_02)
        if ENEMY_02.x < WINDOW.width * 0.10 or ENEMY_02.x > WINDOW.width * 0.80:
            ENEMY_02.x -= 5*DIRECTION_02
            DIRECTION_02 *= -1
        
        ENEMY_03.move_x(ENEMIES_SPEED * DIRECTION_03)
        if ENEMY_03.x < WINDOW.width * 0.10 or ENEMY_03.x > WINDOW.width * 0.80:
            ENEMY_03.x -= 5*DIRECTION_03
            DIRECTION_03 *= -1
    

        ## BLOCK INFERIOR

        ENEMY_04.move_x(ENEMIES_SPEED * DIRECTION_04)
        if ENEMY_04.x < WINDOW.width * 0.25 or ENEMY_04.x > WINDOW.width * 0.95:
            ENEMY_04.x -= 5*DIRECTION_04
            DIRECTION_04 *= -1

        ENEMY_05.move_x(ENEMIES_SPEED * DIRECTION_05)
        if ENEMY_05.x < WINDOW.width * 0.25 or ENEMY_05.x > WINDOW.width * 0.95:
            ENEMY_05.x -= 5*DIRECTION_05
            DIRECTION_05 *= -1

        ENEMY_06.move_x(ENEMIES_SPEED * DIRECTION_06)
        if ENEMY_06.x < WINDOW.width * 0.25 or ENEMY_06.x > WINDOW.width * 0.95:
            ENEMY_06.x -= 5*DIRECTION_06
            DIRECTION_06 *= -1


        ## BLOCO DIREITO

        ENEMY_07.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_07)
        if ENEMY_07.y < WINDOW.height * 0.25 or ENEMY_07.y > WINDOW.height * 0.75:
            ENEMY_07.y -= 5*DIRECTION_07
            DIRECTION_07 *= -1
        
        ENEMY_08.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_08)
        if ENEMY_08.y < WINDOW.height * 0.25 or ENEMY_08.y > WINDOW.height * 0.75:
            ENEMY_08.y -= 5*DIRECTION_08
            DIRECTION_08 *= -1
        
        ENEMY_09.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_09)
        if ENEMY_09.y < WINDOW.height * 0.25 or ENEMY_09.y > WINDOW.height * 0.75:
            ENEMY_09.y -= 5*DIRECTION_09
            DIRECTION_09 *= -1
        
        ENEMY_10.move_y((ENEMIES_SPEED + BONUS_VEL)* DIRECTION_10)
        if ENEMY_10.y < WINDOW.height * 0.25 or ENEMY_10.y > WINDOW.height * 0.75:
            ENEMY_10.y -= 5*DIRECTION_10
            DIRECTION_10 *= -1
        
        ENEMY_11.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_11)
        if ENEMY_11.y < WINDOW.height * 0.25 or ENEMY_11.y > WINDOW.height * 0.75:
            ENEMY_11.y -= 5*DIRECTION_11
            DIRECTION_11 *= -1


        ## BLOCO ESQUERDO

        ENEMY_12.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_12)
        if ENEMY_12.y < WINDOW.height * 0.27 or ENEMY_12.y > WINDOW.height * 0.7:
            ENEMY_12.y -= 5*DIRECTION_12
            DIRECTION_12 *= -1
        
        ENEMY_13.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_13)
        if ENEMY_13.y < WINDOW.height * 0.27 or ENEMY_13.y > WINDOW.height * 0.7:
            ENEMY_13.y -= 5*DIRECTION_13
            DIRECTION_13 *= -1

        ENEMY_14.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_14)
        if ENEMY_14.y < WINDOW.height * 0.27 or ENEMY_14.y > WINDOW.height * 0.7:
            ENEMY_14.y -= 5*DIRECTION_14
            DIRECTION_14 *= -1

        ENEMY_15.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_15)
        if ENEMY_15.y < WINDOW.height * 0.27 or ENEMY_15.y > WINDOW.height * 0.7:
            ENEMY_15.y -= 5*DIRECTION_15
            DIRECTION_15 *= -1
        
        ENEMY_16.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_16)
        if ENEMY_16.y < WINDOW.height * 0.27 or ENEMY_16.y > WINDOW.height * 0.7:
            ENEMY_16.y -= 5*DIRECTION_16
            DIRECTION_16 *= -1

        ENEMY_17.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_17)
        if ENEMY_17.y < WINDOW.height * 0.27 or ENEMY_17.y > WINDOW.height * 0.7:
            ENEMY_17.y -= 5*DIRECTION_17
            DIRECTION_17 *= -1

        ENEMY_18.move_y((ENEMIES_SPEED + BONUS_VEL) * DIRECTION_18)
        if ENEMY_18.y < WINDOW.height * 0.27 or ENEMY_18.y > WINDOW.height * 0.7:
            ENEMY_18.y -= 5*DIRECTION_18
            DIRECTION_18 *= -1




        """
        CHECAGEM DE VITÓRIA
        """

        if COINS >= 18 and PLAYER.collided(WIN_AREA):
            WIN = True

        if WIN:
            while not KEYBOARD.key_pressed("ESC"):
                WINDOW.set_background_color((255, 248, 225))
                WINDOW.draw_text("YOU WIN!", WINDOW.width / 2 - 235, WINDOW.height / 2 - 100, 100, (230, 223, 0), "VCR OSD Mono")
                WINDOW.draw_text("{} deaths".format(DEATHS), WINDOW.width / 2 - 85, WINDOW.height / 2 + 10, 30, (230, 223, 0), "VCR OSD Mono")
                WINDOW.update() 
            
            game(DIFICULDADE_ATUAL + 0.75, WINDOW, KEYBOARD)

        WINDOW.update()
        WINDOW.set_background_color((255, 248, 225))
        if KEYBOARD.key_pressed("ESC"):
            break
