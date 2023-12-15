import pygame
from pygame.locals import *
from sys import exit

pygame.init()

x = 640
y = 480

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Criando objetos')

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (0, 0, 255), (x/2, y/2, 50, 50))
    pygame.draw.circle(tela, (255, 255, 255), (x/4, y/4), 40)
    pygame.display.update()

