import pygame
import sys
import math
import random

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_walk_images = [pygame.image.load("Individual Sprites/adventurer-run-00.png"),
                      pygame.image.load('Individual Sprites/adventurer-run-01.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-02.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-03.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-04.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-05.png')]

player_idle_images = [pygame.image.load("Individual Sprites/adventurer-idle-00.png"),
                      pygame.image.load('Individual Sprites/adventurer-idle-01.png'),
                      pygame.image.load('Individual Sprites/adventurer-idle-02.png'),
                      pygame.image.load('Individual Sprites/adventurer-idle-03.png')]


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        self.moving_vertical = False

    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(
                pygame.transform.flip(player_walk_images[self.animation_count // 4], True, False), (64, 84)),
                         (self.x, self.y))
        elif self.moving_vertical:
            display.blit(pygame.transform.scale(
                pygame.transform.flip(player_walk_images[self.animation_count // 4], True, False), (64, 84)),
                (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (64, 84)), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_idle_images[self.animation_count//4], (64, 84)), (self.x, self.y))


        #pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.moving_right = False
        self.moving_left = False
        self.moving_vertical = False


class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.width = mouse_x
        self.height = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, (0, 0, 0), (self.x, self.y), 5)


class SlimeEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load("Individual Sprites/slime-move-0.png"),
                                 pygame.image.load('Individual Sprites/slime-move-1.png'),
                                 pygame.image.load('Individual Sprites/slime-move-2.png'),
                                 pygame.image.load('Individual Sprites/slime-move-3.png')]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150)

    def main(self, display):
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-150, 150)
            self.offset_y = random.randrange(-150, 150)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1
        if player.x + self.offset_x > self.x-display_scroll[0]:
            self.x += 1
        elif player.x + self.offset_x < self.x-display_scroll[0]:
            self.x -= 1

        if player.y + self.offset_y > self.y-display_scroll[1]:
            self.y += 1
        elif player.y + self.offset_y < self.y-display_scroll[1]:
            self.y -= 1

        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//4], (64, 60)),
                     (self.x-display_scroll[0], self.y-display_scroll[1]))


enemies = [SlimeEnemy(400, 300)]
player = Player(400, 300, 32, 32)

display_scroll = [0, 0]

player_bullets = []

while True:
    display.fill((24, 164, 86))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

    keys = pygame.key.get_pressed()

    pygame.draw.rect(display, (255, 255, 255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

    if keys[pygame.K_d]:
        display_scroll[0] += 5
        for bullet in player_bullets:
            bullet.x -= 5
        player.moving_left = True

    if keys[pygame.K_a]:
        display_scroll[0] -= 5
        for bullet in player_bullets:
            bullet.x += 5
        player.moving_right = True

    if keys[pygame.K_s]:
        display_scroll[1] += 5
        for bullet in player_bullets:
            bullet.y -= 5
        player.moving_vertical = True

    if keys[pygame.K_w]:
        display_scroll[1] -= 5
        for bullet in player_bullets:
            bullet.y += 5
        player.moving_vertical = True

    player.main(display)

    for bullet in player_bullets:
        bullet.main(display)

    for enemy in enemies:
        enemy.main(display)


    clock.tick(60)
    pygame.display.update()
