## Tentativa de jogo ##

#Importa e inicia pygame
import pygame
import sys
from quartz import *
pygame.init()

tela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Project Q.W.A.R.T.Z')
clock = pygame.time.Clock()

player = Player(400,300,32,32)

while True:
    
    tela.fill((0,150,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    
    player.main(tela)
            
        
    
    
    
    
    
    
    
    
    
    clock.tick(60)
    pygame.display.update()