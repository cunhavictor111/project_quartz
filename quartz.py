## FUNCOES QUARTZ
import pygame
import sys

class Player:
    def __init__ (self, x, y, larg, alt):
        self.x = x
        self.y = y
        self.larg = larg
        self.alt = alt
    def main(self,tela):
        pygame.draw.rect(tela, (255,0,0), (self.x, self.y, self.larg, self.alt))