from bullet import *
from shadow import *
from configconst import *
from hud import Hud
from score import Score
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, surf):
        super(Player, self).__init__()
        self.anim_index = 1
        self.surface = surf
        # Plane
        self.dmg = random.randint(8,11)
        self.image = pygame.transform.scale(pygame.image.load("resources/PlayerShip.png"), (100, 100))
        self.image.set_colorkey((33, 33, 33))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 10
        self.shadow = Shadow(self)
        self.speed = 17
        self.dir = None
        self.hp = 2
        self.hud = Hud(self.hp)
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.bullet_cd = 20
        self.score = Score(self.surface)
        self.explosion_frame_rate = 2
        self.is_dead = False

    def update(self):
        if self.is_dead:
            self.death()
        else:
            # Bullets update
            if self.bullet_cd < 1:
                self.bullet_cd = 20
                self.shoot()
            else:
                self.bullet_cd -= 1
            self.hud_group.update()
            # plane and shadow follow the mouse
            mouseX, mouseY = pygame.mouse.get_pos()
            # Vector from plane to cursor
            dx = mouseX - self.rect.centerx
            dy = mouseY+60 - self.rect.bottom
            # Right top
            if dx > 0 and dy < 0:
                self.dir = "RT"
            # Right bottom
            elif dx > 0 and dy > 0:
                self.dir = "RB"
            # Left top
            elif dx < 0 and dy < 0:
                self.dir = "LT"
            # Left bottom
            elif dx < 0 and dy > 0:
                self.dir = "LB"
            # Top
            elif dx == 0 and dy < 0:
                self.dir = "T"
            # Bottom
            elif dx == 0 and dy > 0:
                self.dir = "B"
            # Left
            elif dx < 0 and dy == 0:
                self.dir = "L"
            # Right
            elif dx > 0 and dy == 0:
                self.dir = "R"

            angle = math.atan2(dy, dx)
            distance_travel_x = self.speed * math.cos(angle)
            distance_travel_y = self.speed * math.sin(angle)
            calculated_x = self.rect.centerx + distance_travel_x
            calculated_y = self.rect.centery + distance_travel_y
            if (self.dir == "RT" and calculated_x> mouseX and calculated_y < mouseY) or (self.dir == "LT" and calculated_x < mouseX and calculated_y < mouseY) or (self.dir == "RB" and calculated_x > mouseX and calculated_y > mouseY) or (self.dir == "LB" and calculated_x < mouseX and calculated_y > mouseY) or (self.dir == "T" and calculated_y <= mouseY) or (self.dir == "B" and calculated_y >= mouseY) or (self.dir == "L" and calculated_x <= mouseX) or (self.dir == "R" and calculated_x >= mouseX):
                self.rect.centerx = mouseX
                self.rect.centery = mouseY
            else:
                self.rect.centerx = calculated_x
                self.rect.centery = calculated_y

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top +45)
        bullets_group.add(bullet)

    def get_hit(self, dmg):
        self.hp -= dmg
        self.surface.blit(pygame.transform.scale(hurt_effect_image, (WIDTH, HEIGHT)), (0, 0))
        self.hud.health_bar.decrease_hp(dmg)
        if self.hp <= 0:
            self.is_dead = True
            self.anim_explosion()
            self.death()

    def anim_explosion(self):
        self.explosion = SpriteSheet("resources/ShipExplosion.png", "resources/ShipExplosion.xml")
        self.anim_explosion = []
        frame_name = "tile"
        number = 1
        for frame in range(63):
            fname = f"{frame_name}{number:03}.png"
            new_image = self.explosion.get_image_name(fname)
            new_image_width = new_image.get_width()
            new_image_height = new_image.get_height()
            self.anim_explosion.append(pygame.transform.scale(new_image, (new_image_width //2, new_image_height //2)))
            number += 1

    def death(self):
        if self.anim_index == self.anim_explosion.__len__() -1:
            self.kill()
        self.explosion_frame_rate -=1
        if self.explosion_frame_rate == 0:
            self.image = self.anim_explosion[self.anim_index]
            self.anim_index += 1
            self.explosion_frame_rate = 1
