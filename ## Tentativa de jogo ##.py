## Tentativa de jogo ##

#Importa e inicia pygame
import pygame
import sys
from quartz import *
pygame.init()

#Inicia assets
tela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Project Q.W.A.R.T.Z')

image = pygame.image.load('assets/img/grass.jpg').convert()
image = pygame.transform.scale(image, (1920,1080))

clock = pygame.time.Clock()

player = Player(400,300,32,32)
velx = 5
vely = velx

tela_scroll = [0,0]

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
    
    
    pygame.draw.rect(tela, (255,255,255), (100-tela_scroll[0],100-tela_scroll[1], 16, 16))
    
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
    
    for tiro in tiros_player:
        tiro.main(tela)
            
        
    
    
    

    
    
    
    
    clock.tick(60)
    pygame.display.update()