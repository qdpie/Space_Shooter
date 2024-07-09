import pygame
import os
import random
import constants as c


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.image = pygame.image.load(os.path.join("Images", "enemy_1.png")).convert_alpha()
        self.blow_up_snd = pygame.mixer.Sound(os.path.join("Sounds", "blow_up.ogg"))
        pygame.mixer.Sound.set_volume(self.blow_up_snd, 0.1)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3 ))
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.x = random.randrange(0, c.WINDOW_WIDTH - self.width)
        self.rect.y = 0 - self.height
        self.hp = 1
        self.vel_x = 0
        self.vel_y = random.randrange(2, 6)

    def update(self):
        if self.rect.x > c.WINDOW_HEIGHT:
            self.kill()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        pygame.mixer.Sound.play(self.blow_up_snd)
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()

