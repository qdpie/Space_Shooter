import pygame
from enemy_1 import Enemy1
from enemy_2 import Enemy2
from boss_enemy import BossEnemy
import random


class EnemySpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_1_timer = random.randrange(30, 90)
        self.spawn_2_timer = random.randrange(300, 320)
        self.spawn_3_timer = random.randrange(900, 950)

    def update(self):
        self.enemy_group.update()

        # Spawning enemy 1
        if self.spawn_1_timer == 0:
            self.spawn_enemy1()
            self.spawn_1_timer = random.randrange(30, 90)

        else:
            self.spawn_1_timer -= 1

        # Spawning enemy 2
        if self.spawn_2_timer == 0:
            self.spawn_enemy2()
            self.spawn_2_timer = random.randrange(300, 320)

        else:
            self.spawn_2_timer -= 1

        # Spawning boss
        if self.spawn_3_timer == 0:
            self.spawn_boss_enemy()
            self.spawn_3_timer = random.randrange(900, 950)

        else:
            self.spawn_3_timer -= 1

    def spawn_enemy1(self):
        new_enemy = Enemy1()
        self.enemy_group.add(new_enemy)

    def spawn_enemy2(self):
        new_enemy = Enemy2()
        self.enemy_group.add(new_enemy)

    def spawn_boss_enemy(self):
        new_enemy = BossEnemy()
        self.enemy_group.add(new_enemy)

