import pygame
import os
import random
from bullet import Bullet
import constants as c


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.image = pygame.image.load(os.path.join("Images", "enemy_2.png"))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.x = random.randrange(0, c.WINDOW_WIDTH - self.width)
        self.rect.y = 0 - self.height
        self.hp = 3
        self.vel_x = 0
        self.vel_y = random.randrange(2, 4)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.y >= 180 - self.height:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = random.randrange(-4, 4)
        if self.rect.x <= -20:
            self.vel_x *= -1
        elif self.rect.x + self.rect.width >= c.WINDOW_WIDTH + 20:
            self.vel_x *= -1

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
