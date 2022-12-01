#Sprites
import pygame

#Cria um display
display = pygame.display.set_mode((800, 600))

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