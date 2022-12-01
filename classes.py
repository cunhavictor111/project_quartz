import pygame
import math
import random
from sprites import *

# define contador
def cronos():
    cloc = pygame.time.Clock()
    minutes = 0
    seconds = 0
    mili = 0

    while True:
        if mili > 1000:
            seconds += 1
            mili -= 1000
        if seconds > 60:
            minutes += 1
            seconds -= 60

        mili += cloc.tick_busy_loop(60)


# Classifica personagem do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.x = 400 - 30
        self.y = 300 - 30
        self.image = img
        self.rect = self.image.get_rect()
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        self.moving_vertical = False

    # define arma do jogador
    def handle_weapons(self, display):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.scale(player_weapon, (80, 80))
        player_weapon_copy_2 = pygame.transform.rotate(player_weapon_copy, angle)

        display.blit(player_weapon_copy_2, (self.x + 45 - int(player_weapon_copy_2.get_width() / 2),
                                            self.y + 25 - int(player_weapon_copy_2.get_height() / 2)))

    # define animação de andar e arma na tela
    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(
                pygame.transform.flip(player_walk_images[self.animation_count // 4], True, False), (75, 61)),
                (self.x, self.y))
        elif self.moving_left and self.moving_vertical:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count // 4], (75, 61)),
                         (self.x, self.y))
        elif self.moving_vertical:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count // 4], (75, 61)),
                         (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count // 4], (75, 61)),
                         (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_idle_images[self.animation_count // 4], (75, 61)),
                         (self.x, self.y))

        self.handle_weapons(display)

        # pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.moving_right = False
        self.moving_left = False
        self.moving_vertical = False


# classifica projétil
class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y, img):
        pygame.sprite.Sprite.__init__(self)
        self.x = x - 20
        self.y = y - 20
        self.width = mouse_x
        self.height = mouse_y
        self.image = img
        self.rect = self.image.get_rect()
        self.speed = 10
        self.animation_count = 0
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        self.posi_x = 0
        self.posi_y = 0

    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        if self.animation_count + 1 >= 7:
            self.animation_count = 0
        self.animation_count += 1
        if self.animation_count < 8:
            display.blit(pygame.transform.scale(player_fireball2[self.animation_count // 3], (150, 122)),
                         (self.x, self.y))
        self.posi_x -= int(self.x_vel)
        self.posi_y -= int(self.y_vel)


# classifica slime / inimigo
class SlimeEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.image = img
        self.rect = self.image.get_rect()
        self.y = y
        # define sprites do slime
        self.animation_images = [pygame.image.load("Individual Sprites/slime-move-0.png"),
                                 pygame.image.load('Individual Sprites/slime-move-1.png'),
                                 pygame.image.load('Individual Sprites/slime-move-2.png'),
                                 pygame.image.load('Individual Sprites/slime-move-3.png')]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = 0
        self.offset_y = 0
        self.pos_x = 0
        self.pos_y = 0

    def main(self, display):  # offset e movimentação do inimigo
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = 0
            self.offset_y = 0
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1
        if player.x + self.offset_x > self.x - display_scroll[0]:
            self.x += 4
        elif player.x + self.offset_x < self.x - display_scroll[0]:
            self.x -= 4

        if player.y + self.offset_y > self.y - display_scroll[1]:
            self.y += 4
        elif player.y + self.offset_y < self.y - display_scroll[1]:
            self.y -= 4

        self.pos_x = self.x - display_scroll[0]
        self.pos_y = self.y - display_scroll[1]
        # coloca inimigo na tela
        display.blit(pygame.transform.scale(self.animation_images[self.animation_count // 4], (64, 60)),
                     (self.x - display_scroll[0], self.y - display_scroll[1]))

# Criando Grupos#

all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

# Criando player
player = Player(player_image)
all_sprites.add(player)

# Criando inimigos#
randx = random.randint(0, 800)
randy = random.randint(0, 600)

display_scroll = [0, 0]
