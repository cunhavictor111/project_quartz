## FUNCOES QUARTZ
import pygame
import sys
import math
class Player:
    def __init__ (self, x, y, larg, alt):
        self.x = x
        self.y = y
        self.larg = larg
        self.alt = alt
    def main(self,tela):
        pygame.draw.rect(tela, (255,0,0), (self.x, self.y, self.larg, self.alt))
        

class TiroJog:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.width = mouse_x
        self.height = mouse_y
        self.speed = 15
        self.ang = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.ang)* self.speed
        self.y_vel = math.sin(self.ang)* self.speed
        
    def main(self,tela):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        
        pygame.draw.circle(tela, (0,0,0), (self.x, self.y), 5)
        