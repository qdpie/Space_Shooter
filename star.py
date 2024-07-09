import pygame
import random
import constants as c
import all_the_colors as color


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        # ygyself.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.color = (color.LIGHT_YELLOW_3)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.WINDOW_WIDTH)
        self.vel_x = 0
        self.vel_y = random.randrange(5, 25)

    def update(self):
        if self.rect.x > c.WINDOW_HEIGHT:
            self.kill()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
