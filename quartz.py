## FUNCOES QUARTZ
import pygame
from pygame.locals import *
import sys
import math
import random

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

class Enemy:
    def __init__(self,x,y,width,height):
        pos = ['x','y']
        pos = random.choice(pos)
        if pos == 'x':
            x = 0
        else:
            y = 0
        self.x = random.randint(0,x)
        if x == 0:
            self.x = 0
        self.y = random.randint(0,y)
        if y == 0:
            self.y = 0
        self.width = width
        self.height = height

    def main(self,tela,scroll):
        pygame.draw.rect(tela, (255,255,255), (self.x-scroll[0],self.y-scroll[1],self.width,self.height))
    
    def move_to_player(self,player):
        