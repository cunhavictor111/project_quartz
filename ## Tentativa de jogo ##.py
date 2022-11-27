## Tentativa de jogo ##

#Importa e inicia pygame
import pygame
import sys
from quartz import *
from gerador_de_inimigos import *
pygame.init()

#Inicia assets
WIDTH = 800
HEIGHT = 600
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Project Q.W.A.R.T.Z')

image = pygame.image.load('assets/img/grass.jpg').convert()
image = pygame.transform.scale(image, (1920,1080))

clock = pygame.time.Clock()

tela_scroll = [0,0]

player = Player(400,300,32,32)
enemy = Enemy(800,600,16,16)
velx = 5
vely = velx


tiros_player = []

while True:
    
    tela.fill((24,150,86))
    keys = pygame.key.get_pressed()
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        if keys[pygame.K_ESCAPE]:
            sys.exit()
            pygame.QUIT
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                tiros_player.append(TiroJog(player.x, player.y, mouse_x, mouse_y))
    
    
    
    
    if keys[pygame.K_a]:
        tela_scroll[0] -= velx
        for tiro in tiros_player:
            tiro.x += 5
    if keys[pygame.K_d]:
        tela_scroll[0] += velx
        for tiro in tiros_player:
            tiro.x -= 5
    if keys[pygame.K_s]:
        tela_scroll[1] += vely
        for tiro in tiros_player:
            tiro.y -= 5
    if keys[pygame.K_w]:
        tela_scroll[1] -= vely
        for tiro in tiros_player:
            tiro.y += 5
        
    
    player.main(tela)
    enemy.main(tela,tela_scroll)
    
    for tiro in tiros_player:
        TiroJog.main(tela)
            
        
    
    
    

    
    
    
    
    clock.tick(60)
    pygame.display.update()