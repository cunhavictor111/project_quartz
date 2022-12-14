# importa parâmetros
import pygame
import sys
import math
import random
import time

# inicia mixer
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

# carrega e toca música
pygame.mixer.music.load('xDeviruchi - 8-bit Fantasy  & Adventure Music (2021)/xDeviruchi - Minigame .wav')
assets = {}
assets['hit_sound'] = pygame.mixer.Sound('hit.wav')
pygame.mixer.music.play(loops=2, start=0.0)

# define tela
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# importa sprites
player_walk_images = [pygame.image.load("Individual Sprites/adventurer-run-00.png"),
                      pygame.image.load('Individual Sprites/adventurer-run-01.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-02.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-03.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-04.png'),
                      pygame.image.load('Individual Sprites/adventurer-run-05.png')]

player_image = (pygame.image.load('Individual Sprites/adventurer-run-00.png'))
player_image = pygame.transform.scale(player_image, (32, 32))

player_idle_images = [pygame.image.load("Individual Sprites/adventurer-idle-00.png"),
                      pygame.image.load('Individual Sprites/adventurer-idle-01.png'),
                      pygame.image.load('Individual Sprites/adventurer-idle-02.png'),
                      pygame.image.load('Individual Sprites/adventurer-idle-03.png')]

player_fireball2 = [pygame.image.load("Individual Sprites/shoot1.png"),
                    pygame.image.load("Individual Sprites/shoot2.png"),
                    pygame.image.load("Individual Sprites/shoot3.png"),
                    pygame.image.load("Individual Sprites/shoot4.png")]
fireball = (pygame.image.load("Individual Sprites/shoot1.png"))
fireball = pygame.transform.scale(fireball, (20, 20))
slimeimg = pygame.image.load('Individual Sprites/slime-move-0.png')
slimeimg = pygame.transform.scale(slimeimg, (60, 60))

player_weapon = pygame.image.load("Individual Sprites/staff.png").convert()
player_weapon.set_colorkey((0, 0, 0))


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

# cria spawn de inimigos em intervalos regulares
while len(all_enemies) != 5:
    randx = random.randint(0, 800)
    randy = random.randint(0, 600)
    slime = SlimeEnemy(randx, randy, slimeimg)
    all_enemies.add(slime)
    all_sprites.add(slime)

player_bullets = pygame.sprite.Group()

last_update = pygame.time.get_ticks()
game = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
life = 50
pontos = 0
pontosa = 0

# inicia jogo
while game:
    #  colore tela e coloca pontuação na tela
    font = pygame.font.SysFont('Stencil', 48)
    text = font.render(f'{pontos}', True, (0, 0, 0))
    display.fill((24, 164, 86))
    display.blit(text, (10, 10))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

        # define botão de tiro no mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.add(PlayerBullet(player.x, player.y, mouse_x, mouse_y, fireball))

    # colisão da bala com slime
    for bullet in player_bullets:
        bullet_rect = pygame.Rect(bullet.x, bullet.y, 20, 20)
        for enemy in all_enemies:
            enemy_rect = pygame.Rect(enemy.pos_x, enemy.pos_y, 32, 32)
            if pygame.Rect.colliderect(bullet_rect, enemy_rect):
                assets['hit_sound'].play()
                enemy.kill()
                bullet.kill()
                pontos += 1
                print(pontos)

    # sistema de regeneração de vida
    if pontos % 20 == 0 and pontos != pontosa:
        life += 10
        pontosa = pontos
    if life > 50:
        life = 50

    keys = pygame.key.get_pressed()
    now = pygame.time.get_ticks()

    if now - last_update > 150:
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        slime = SlimeEnemy(-x, -y, slimeimg)
        all_enemies.add(slime)
        all_sprites.add(slime)
        last_update = now

    # movimento do personagem
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

    all_sprites.update()

    player.main(display)

    for z in all_enemies:
        z.main(display)

    pygame.display.update()

    for bullet in player_bullets:
        bullet.main(display)

    # colisão do personagem com inimigo
    rect_player = pygame.Rect(400, 300, 32, 32)
    for enemy in all_enemies:
        enemy_rect = pygame.Rect(enemy.pos_x, enemy.pos_y, 32, 32)
        if pygame.Rect.colliderect(rect_player, enemy_rect):
            if life > 1:
                life -= 0.5
                print(f"Vidas restantes: {life}")
            elif life <= 1:
                font2 = pygame.font.SysFont('stencil', 70)
                text = font2.render('Game Over', True, (255, 0, 0))
                display.fill((0, 0, 0))
                display.blit(text, (200, 260))
                text2 = font2.render('Score: {0}'.format(pontos), True, (255, 0, 0))
                display.blit(text2, (200, 190))
                pygame.display.update()
                time.sleep(3)
                game = False

    # coloca barra de vida
    pygame.draw.rect(display, RED, (382, 260, 50, 10))
    pygame.draw.rect(display, GREEN, (382, 260, (life * 2 // 2), 10))

    clock.tick(60)
    pygame.display.update()
