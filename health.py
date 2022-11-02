import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(HealthBar, self).__init__()
        self.max_hp = hp
        self.hp = self.max_hp
        self.image = pygame.image.load("resources/UI_Health.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() //2 + 17, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.y = 8
        self.rect.x = 33
        self.velX = 0
        self.velY = 0
        self.max_width = self.image.get_width()

    def update(self):
        self.rect.x += self.velX
        self.rect.y += self.velY

    def decrease_hp(self, dmg):
        self.hp -= dmg
        self.image = pygame.transform.scale(self.image, (self.max_width * self.hp // self.max_hp, self.image.get_height()))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
