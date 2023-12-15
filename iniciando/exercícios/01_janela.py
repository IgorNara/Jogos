import pygame
from pygame.locals import *
from sys import exit

pygame.init()

x = 640
y = 480

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Criando janela')

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    
