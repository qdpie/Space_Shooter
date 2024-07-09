import pygame
import all_the_colors as color


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.width = 4
        self.height = 10
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = color.RED
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = -10

    def update(self):
        if self.rect.x < 0:
            self.kill()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

