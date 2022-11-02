from shadow import *
from configconst import *


class Mob(pygame.sprite.Sprite):
    # mob sprite - spawns above top and moves downward
    def __init__(self):
        super(Mob, self).__init__()
        self.anim_index = 0
        self.type_plane = f"Type {str(random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], mobImg_weight)[0] + 1)}"
        self.image = pygame.transform.scale(mobImg.get(self.type_plane).get("Img"), (70, 70))
        self.image.set_colorkey((140, 140, 132))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-80, -50)
        self.velY = random.randrange(1, 3)
        self.shadow = Shadow(self)
        self.max_hp = mobImg.get(self.type_plane).get("Max_Hp")
        self.hp = self.max_hp
        self.is_destroyed = False
        self.explosion_frame_rate = 2
        self.dmg_value = 2


    def update(self):
        if self.is_destroyed:
            self.destroy()
        else:
            self.rect.y += self.velY
        if self.rect.top > HEIGHT + 10:
            self.rect.y = random.randrange(-80, -50)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.velY = random.randrange(1, 8)


    def anim_explosion(self):
        self.explosion = SpriteSheet("resources/explosion.png", "resources/explosion.xml")
        self.anim_explosion = []
        frame_name = "tile"
        number = 0
        angle = random.randint(0, 360)
        for frame in range(13):
            fname = f"{frame_name}{number:03}.png"
            new_image = self.explosion.get_image_name(fname)
            new_image_width = new_image.get_width()
            new_image_height = new_image.get_height()
            self.anim_explosion.append(pygame.transform.rotate(
                pygame.transform.scale(new_image, (new_image_width - 80, new_image_height - 80)), angle))
            number += 1

    def get_hit(self, dmg):
        if not self.is_destroyed:
            bullet_hit.play()
            self.hp -= dmg
            if(self.hp <= 0):
                self.is_destroyed = True
                self.anim_explosion()
                explode.play()
                self.velY = 0
                self.rect.x = self.rect.x - 10
                self.rect.y = self.rect.y - 5
        else:
            pass

    def destroy(self):
        if self.anim_index == self.anim_explosion.__len__() - 1:
            self.kill()
        self.explosion_frame_rate -= 1
        if self.explosion_frame_rate == 0:
            self.image = self.anim_explosion[self.anim_index]
            self.anim_index += 1
            self.explosion_frame_rate = 2
