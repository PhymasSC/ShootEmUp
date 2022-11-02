from mob import Mob
import pygame
import random

class MobSpawner:
    def __init__(self):
        self.mob_group = pygame.sprite.Group()
        self.hp_bar_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(120, 360)
        self.mob = Mob()
        self.mob_group.add(self.mob)


    def update(self):
        self.mob_group.update()
        self.hp_bar_group.update(self.mob.rect.x, self.mob.rect.y)
        if self.spawn_timer == 0:
            self.spawn_mob()
            self.spawn_timer = random.randrange(30, 120)
        else:
            self.spawn_timer -= 1

    def spawn_mob(self):
        new_enemy = Mob()
        self.mob_group.add(new_enemy)
