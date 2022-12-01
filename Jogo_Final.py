# importa parâmetros
import pygame
import sys
import math
import random
import time
from sprites import *
from classes import *

# inicia mixer
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

# carrega e toca música
pygame.mixer.music.load('xDeviruchi - 8-bit Fantasy  & Adventure Music (2021)/xDeviruchi - Minigame .wav')
pygame.mixer.music.play(loops=2, start=0.0)


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
