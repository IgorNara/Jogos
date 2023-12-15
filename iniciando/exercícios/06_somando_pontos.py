import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
x_verde =  randint(40, 600)
y_verde = randint(50, 430)

fonte = pygame.font.SysFont('arial', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('Colisão de objetos')

while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x -= 5
        #     if event.key == K_d:
        #         x += 5
        #     if event.key == K_s:
        #         y += 5
        #     if event.key == K_w:
        #         y -= 5
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x -= 5
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x += 5
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y += 5
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y -= 5
    
    azul = pygame.draw.rect(tela, (0, 0, 255), (x, y, 40, 50))
    verde = pygame.draw.rect(tela, (0, 255, 0), (x_verde, y_verde, 40, 50))

    if azul.colliderect(verde):
        x_verde =  randint(40, 600)
        y_verde = randint(50, 430)
        pontos += 1 

    tela.blit(texto_formatado, (430, 40))
    pygame.display.update()

