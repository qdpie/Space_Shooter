import pygame
import constants as c
import os
from bullet import Bullet


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super(SpaceShip, self).__init__()
        self.shoot_snd = pygame.mixer.Sound(os.path.join("Sounds", "shoot_snd.ogg"))
        pygame.mixer.Sound.set_volume(self.shoot_snd, 0.1)
        self.image = pygame.image.load(os.path.join("Images", "spaceship.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.x = c.WINDOW_WIDTH // 2 - self.rect.width // 2
        self.rect.y = c.WINDOW_HEIGHT - self.rect.height - self.rect.height
        self.bullets = pygame.sprite.Group()
        self.vel_x = 0
        self.vel_y = 0
        self.movement = pygame.math.Vector2(0, 0)
        self.movement_speed = 8

    def ship_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.movement.x = -self.movement_speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.movement.x = self.movement_speed
        else:
            self.movement.x = 0

    def Shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + self.rect.width // 2
        new_bullet.rect.y = self.rect.y + self.rect.height - 50
        self.bullets.add(new_bullet)
        pygame.mixer.Sound.play(self.shoot_snd)

    def update(self):
        self.bullets.update()
        self.ship_movement()
        self.rect.x += self.movement.x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.WINDOW_WIDTH - self.rect.width:
            self.rect.x = c.WINDOW_WIDTH - self.rect.width
        self.rect.x += self.vel_y







