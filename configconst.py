import os
import random

import pygame
from win32api import GetSystemMetrics

from spritesheet import SpriteSheet

DESKTOP_WIDTH = GetSystemMetrics(0)
DESKTOP_HEIGHT = GetSystemMetrics(1)

WIDTH = 360
HEIGHT = 640
TITLE = "Shoot'em up"
SUN_POSITION = (180, -200)
# Set windows position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (DESKTOP_WIDTH // 2 - WIDTH // 2, DESKTOP_HEIGHT // 2 - HEIGHT // 2)

# initialize pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption(TITLE)
pygame.mouse.set_visible(False)
pygame.display.set_icon(pygame.image.load("resources/logo.png"))
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()

# load graphics
back = []
mobImg = []
for i in range(29):
        back.append(f"resources/Background{i}.png")

enemy_sprites = SpriteSheet("resources/EnemySprites.png", "resources/EnemySprites.xml")
mobImg = {"Type 1": {"Img": enemy_sprites.get_image_name("Enemy_1.png").convert_alpha(),
                     "Max_Hp": 20},
          "Type 2": {"Img": enemy_sprites.get_image_name("Enemy_2.png").convert_alpha(),
                     "Max_Hp": 24},
          "Type 3": {"Img": enemy_sprites.get_image_name("Enemy_3.png").convert_alpha(),
                     "Max_Hp": 32},
          "Type 4": {"Img": enemy_sprites.get_image_name("Enemy_4.png").convert_alpha(),
                     "Max_Hp": 50},
          "Type 5": {"Img": enemy_sprites.get_image_name("Enemy_5.png").convert_alpha(),
                     "Max_Hp": 50},
          "Type 6": {"Img": enemy_sprites.get_image_name("Enemy_6.png").convert_alpha(),
                     "Max_Hp": 65},
          "Type 7": {"Img": enemy_sprites.get_image_name("Enemy_7.png").convert_alpha(),
                     "Max_Hp": 80},
          "Type 8": {"Img": enemy_sprites.get_image_name("Enemy_8.png").convert_alpha(),
                     "Max_Hp": 120},
          "Type 9": {"Img": enemy_sprites.get_image_name("Enemy_9.png").convert_alpha(),
                     "Max_Hp": 150},
          "Type 10": {"Img": enemy_sprites.get_image_name("Enemy_10.png").convert_alpha(),
                     "Max_Hp": 100},
          "Type 11": {"Img": enemy_sprites.get_image_name("Enemy_11.png").convert_alpha(),
                     "Max_Hp": 150},
          "Type 12": {"Img": enemy_sprites.get_image_name("Enemy_12.png").convert_alpha(),
                     "Max_Hp": 125},
          "Type 13": {"Img": enemy_sprites.get_image_name("Enemy_13.png").convert_alpha(),
                     "Max_Hp": 120},
          "Type 14": {"Img": enemy_sprites.get_image_name("Enemy_14.png").convert_alpha(),
                     "Max_Hp": 135},
          "Type 15": {"Img": enemy_sprites.get_image_name("Enemy_15.png").convert_alpha(),
                     "Max_Hp": 145},
          "Type 16": {"Img": enemy_sprites.get_image_name("Enemy_16.png").convert_alpha(),
                     "Max_Hp": 150},
          "Type 17": {"Img": enemy_sprites.get_image_name("Enemy_17.png").convert_alpha(),
                     "Max_Hp": 200},
          }

mobImg_weight = [.2, .2, .2, .075,.070, .030 ,.025, .025, .0125, .0125, .0125, .0125, .025, .025, .025, .025, .025]

background = pygame.transform.scale(pygame.image.load(back[random.randint(1, 28)]).convert(), (WIDTH, HEIGHT))

# self.image = pg.Surface((120, 120), pg.SRCALPHA)
# pg.draw.polygon(self.image, (0, 100, 240), [(60, 0), (120, 120), (0, 120)])

hurt_effect_image = pygame.transform.scale(pygame.image.load("resources/Hurt_Effect.png").convert_alpha(), (WIDTH, HEIGHT))

# load sfx
intro = pygame.mixer.Sound("resources/Intro.wav")
explode = pygame.mixer.Sound("resources/Explosion01.wav")
bullet_hit = pygame.mixer.Sound("resources/BulletHit01.wav")

# set up new game
bullets_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# load fonts
userInterface = SpriteSheet("resources/UI.png", "resources/UI.xml")
