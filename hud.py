from health import HealthBar
import pygame

class Hud(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(Hud, self).__init__()
        self.image = pygame.image.load("resources/health_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() //2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.y = 5
        self.rect.x = 5
        self.health_bar = HealthBar(hp)
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)

    def update(self):
        self.health_bar_group.update()