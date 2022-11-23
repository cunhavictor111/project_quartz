#----------Criando um mapa---------#

#Importa e inicia pacotes
import pygame
pygame.init()


clock = pygame.time.Clock()
FPS = 60

#Gerando tela do jogo
window = pygame.display.set_mode((400,500))
pygame.display.set_caption('Project Q.W.A.R.T.Z')

#Estrutura de dados basica

game = True

#Inicia assets

image = pygame.image.load('assets/img/grass.jpg').convert()
image = pygame.transform.scale(image, (1920,1080))

#Loop principal
while game:
    
    clock.tick(FPS)
    
    #Trata eventos
    for event in pygame.event.get():
        #Verifica evento
        if event.type == pygame.KEYDOWN:
            game = False
        if event.type == pygame.QUIT:
            game = False
            
    # ----- Gera saídas ----- #
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (-760,-290))
    
    
    
    #Atualiza estado do jogo
    pygame.display.update()
    
    
# ===== Finalização ===== #
pygame.quit()