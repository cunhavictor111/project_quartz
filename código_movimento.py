import pygame
import sys
import math

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_walk_images = [pygame.image.load("assets/player/run/adventurer-run-00.png"),
                      pygame.image.load('assets/player/run/adventurer-run-01.png'),
                      pygame.image.load('assets/player/run/adventurer-run-02.png'),
                      pygame.image.load('assets/player/run/adventurer-run-03.png'),
                      pygame.image.load('assets/player/run/adventurer-run-04.png'),
                      pygame.image.load('assets/player/run/adventurer-run-05.png')]

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False

    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (64, 84)), (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count // 4], True, False), (64, 84)),
                         (self.x, self.y))

        #pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.moving_right = False
        self.moving_left = False


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

    if keys[pygame.K_a]:
        display_scroll[0] += 5
        for bullet in player_bullets:
            bullet.x -= 5
        player.moving_left = True

    if keys[pygame.K_d]:
        display_scroll[0] -= 5
        for bullet in player_bullets:
            bullet.x += 5
        player.moving_right = True

    if keys[pygame.K_w]:
        display_scroll[1] += 5
        for bullet in player_bullets:
            bullet.y -= 5

    if keys[pygame.K_s]:
        display_scroll[1] -= 5
        for bullet in player_bullets:
            bullet.y += 5

    player.main(display)

    for bullet in player_bullets:
        bullet.main(display)


    clock.tick(60)
    pygame.display.update()