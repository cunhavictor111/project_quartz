import pygame
import sys
import math
import random
import time

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


player_fireball = [pygame.image.load("Individual Sprites/img_0.png"),
                   pygame.image.load("Individual Sprites/img_1.png"),
                   pygame.image.load("Individual Sprites/img_2.png"),
                   pygame.image.load("Individual Sprites/img_3.png"),
                   pygame.image.load("Individual Sprites/img_4.png"),
                   pygame.image.load("Individual Sprites/img_5.png"),
                   pygame.image.load("Individual Sprites/img_6.png"),
                   pygame.image.load("Individual Sprites/img_7.png"),
                   pygame.image.load("Individual Sprites/img_8.png"),
                   pygame.image.load("Individual Sprites/img_9.png"),
                   pygame.image.load("Individual Sprites/img_10.png"),
                   pygame.image.load("Individual Sprites/img_11.png"),
                   pygame.image.load("Individual Sprites/img_12.png"),
                   pygame.image.load("Individual Sprites/img_13.png"),
                   pygame.image.load("Individual Sprites/img_14.png"),
                   pygame.image.load("Individual Sprites/img_15.png"),
                   pygame.image.load("Individual Sprites/img_16.png"),
                   pygame.image.load("Individual Sprites/img_17.png"),
                   pygame.image.load("Individual Sprites/img_18.png"),
                   pygame.image.load("Individual Sprites/img_19.png"),
                   pygame.image.load("Individual Sprites/img_20.png"),
                   pygame.image.load("Individual Sprites/img_21.png"),
                   pygame.image.load("Individual Sprites/img_22.png"),
                   pygame.image.load("Individual Sprites/img_23.png"),
                   pygame.image.load("Individual Sprites/img_24.png"),
                   pygame.image.load("Individual Sprites/img_25.png"),
                   pygame.image.load("Individual Sprites/img_26.png"),
                   pygame.image.load("Individual Sprites/img_27.png"),
                   pygame.image.load("Individual Sprites/img_28.png"),
                   pygame.image.load("Individual Sprites/img_29.png"),
                   pygame.image.load("Individual Sprites/img_30.png"),
                   pygame.image.load("Individual Sprites/img_31.png"),
                   pygame.image.load("Individual Sprites/img_32.png"),
                   pygame.image.load("Individual Sprites/img_33.png"),
                   pygame.image.load("Individual Sprites/img_34.png")]

player_prefire = [pygame.image.load("Individual Sprites/preshoot1.png"),
                  pygame.image.load("Individual Sprites/preshoot2.png"),
                  pygame.image.load("Individual Sprites/preshoot3.png")]

player_fireball2 = [pygame.image.load("Individual Sprites/shoot1.png"),
                    pygame.image.load("Individual Sprites/shoot2.png"),
                    pygame.image.load("Individual Sprites/shoot3.png"),
                    pygame.image.load("Individual Sprites/shoot4.png")]

player_weapon = pygame.image.load("Individual Sprites/Kar98k.png").convert()
player_weapon.set_colorkey((0, 0, 0))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.x = x - 30
        self.y = y - 30
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        self.moving_vertical = False

    def handle_weapons(self, display):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180/math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)

        display.blit(player_weapon_copy, (self.x + 15 - int(player_weapon_copy.get_width()/2),
                                          self.y + 25 - int(player_weapon_copy.get_height()/2)))


    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(
                pygame.transform.flip(player_walk_images[self.animation_count // 4], True, False), (75, 61)),
                         (self.x, self.y))
        elif self.moving_left and self.moving_vertical:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (75, 61)), (self.x, self.y))
        elif self.moving_vertical:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (75, 61)), (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (75, 61)), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_idle_images[self.animation_count//4], (75, 61)), (self.x, self.y))

        self.handle_weapons(display)

        #pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.moving_right = False
        self.moving_left = False
        self.moving_vertical = False


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x + 30
        self.y = y + 30
        self.width = mouse_x
        self.height = mouse_y
        self.speed = 15
        self.animation_count = 0
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        
        if self.animation_count + 1 >= 7:
            self.animation_count = 0
        self.animation_count += 1
        if self.animation_count <=3:
            display.blit(pygame.transform.scale(player_prefire[self.animation_count//3], (75, 61)), (self.x, self.y))
        elif self.animation_count > 3:
            display.blit(pygame.transform.scale(player_fireball2[self.animation_count//4], (75, 61)), (self.x, self.y))


class SlimeEnemy:
    def __init__(self, x, y):
        pos = ['x','y']
        pos = random.choice(pos)
        self.x = random.randint(0,x)
        if pos == 'x':
            self.x = 0
        self.y = random.randint(0,y)
        if pos == 'y':
            self.y = 0
        self.animation_images = [pygame.image.load("Individual Sprites/slime-move-0.png"),
                                 pygame.image.load('Individual Sprites/slime-move-1.png'),
                                 pygame.image.load('Individual Sprites/slime-move-2.png'),
                                 pygame.image.load('Individual Sprites/slime-move-3.png')]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = 0
        self.offset_y = 0

    def main(self, display):
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = 0
            self.offset_y = 0
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


player = Player(400, 300, 32, 32)

display_scroll = [0, 0]

player_bullets = []
    
c = 0
list_enemies = []
while c <= 5:
    x = random.randint(0,800)
    y = random.randint(0,600)
    enemy = SlimeEnemy(x,y)
    list_enemies.append(enemy)
    c += 1

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

    for z in list_enemies:
        z.main(display)

    clock.tick(60)
    pygame.display.update()
