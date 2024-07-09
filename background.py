import pygame
import constants as c
import random
import all_the_colors as color
from star import Star

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.WINDOW_SIZE)
        self.image.fill(color.GREY11)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1, 10)

    def update(self):
        self.stars.update()
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = random.randrange(1, 3)
        self.image.fill(color.GREY11)
        self.stars.draw(self.image)
        self.timer -= 1