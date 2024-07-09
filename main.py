import pygame
from space_ship import SpaceShip
from background import BG
from enemy_spawner import EnemySpawner
import os
import constants as c
import all_the_colors as color

# Display Setup
display = pygame.display.set_mode(c.WINDOW_SIZE)
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load(os.path.join("Images", "spaceship.png")).convert_alpha()
pygame.display.set_icon(icon)
fps = 60
clock = pygame.time.Clock()
background = color.GREY11

# Sound Setup
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init(44100, -16, 2, 2048)
pygame.init()

# Object Setup
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)

player = SpaceShip()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

enemy_spawner = EnemySpawner()


running = True
while running:
    # Tick The Clock
    clock.tick(fps)

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Shooting Event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.Shoot()

    # Update All The Objects (updating the objects in memory)
    sprite_group.update()
    bg_group.update()
    enemy_spawner.update()

    # Check Collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()

    # Render The Display (draw objeacts to the scree)
    display.fill(background)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)

    pygame.display.update()
