import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('Colisão de objetos')

x = int(largura/2)
y = int(altura/2)
x_verde =  randint(40, 600)
y_verde = randint(50, 430)

x_banana = randint(10, 630)
y_banana = -10
x_banana_batizada = randint(10, 630)
y_banana_batizada = -10
vetor_bananas = ["pura", "batizada"]

x_maca = randint(10, 630)
y_maca = -10
x_maca_batizada = randint(10, 630)
y_maca_batizada = -10
vetor_macas = ["pura", "batizada"]

x_pera = randint(10, 630)
y_pera = -10
x_pera_batizada = randint(10, 630)
y_pera_batizada = -10
vetor_peras = ["pura", "batizada"]

x_caju = randint(10, 630)
y_caju = -10
x_caju_batizado = randint(10, 630)
y_caju_batizado = -10
vetor_cajus = ["pura", "batizada"]

x_morango = randint(10, 630)
y_morango = -10
x_morango_batizado = randint(10, 630)
y_morango_batizado = -10
vetor_morangos = ["pura", "batizada"]

som_colisao = pygame.mixer.Sound("som.wav")

velocidade = 7

# fruta = pygame.draw.rect(tela, (0,0,0), (x_fruta, y_fruta, 10, 10))
frutas_tipos = ['banana', 'maça', 'caju', 'pera', 'morango']
frutas_objetos = []

timer = 0

fonte = pygame.font.SysFont('arial', 40, True, False)
pontos = 0

while True:
    relogio.tick(50)
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
    if(pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]) and x > 0:
        x -= 7
    if(pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]) and x < largura-40:
        x += 7
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y += 0
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y -= 0
    azul = pygame.draw.rect(tela, (0, 0, 255), (x, 410, 40, 50))
    banana = pygame.draw.rect(tela, (255,0,0), (x_banana, y_banana, 10, 10))
    banana_batizada = pygame.draw.rect(tela, (255,0,0), (x_banana_batizada, y_banana_batizada, 10, 10))
    maca = pygame.draw.rect(tela, (0,255,0), (x_maca, y_maca, 10, 10))
    maca_batizada = pygame.draw.rect(tela, (0,255,0), (x_maca_batizada, y_maca_batizada, 10, 10))
    pera = pygame.draw.rect(tela, (100,100,100), (x_pera, y_pera, 10, 10))
    pera_batizada = pygame.draw.rect(tela, (100,100,100), (x_pera_batizada, y_pera_batizada, 10, 10))
    caju = pygame.draw.rect(tela, (200,200,200), (x_caju, y_caju, 10, 10))
    caju_batizado = pygame.draw.rect(tela, (200,200,200), (x_caju_batizado, y_caju_batizado, 10, 10))
    morango = pygame.draw.rect(tela, (255,255,255), (x_morango, y_morango, 10, 10))
    morango_batizado = pygame.draw.rect(tela, (255,255,255), (x_morango_batizado, y_morango_batizado, 10, 10))
    # verde = pygame.draw.rect(tela, (0, 255, 0), (x_verde, y_verde, 40, 50))
    if timer < 60:
        timer += 1
    else:
        timer = 0
        i = randint(0, len(frutas_tipos) - 1)
        if frutas_tipos[i] == 'banana':
            j = randint(0, len(vetor_bananas)-1)
            if vetor_bananas[j] == 'pura':
                if y_banana == 0:
                    frutas_objetos.append(banana)
                elif y_banana > altura:
                    y_banana = 0
            else:
                if y_banana_batizada == 0:
                    frutas_objetos.append(banana_batizada)
                else:
                    y_banana_batizada += velocidade
                    if y_banana_batizada > altura:
                        y_banana_batizada = 0

        elif frutas_tipos[i] == 'maça':
            if y_maca == 0:
                j = randint(0, len(vetor_macas)-1)
                if vetor_macas[j] == 'pura':
                    frutas_objetos.append(maca)
                else:
                    frutas_objetos.append(maca_batizada)
            else:
                y_maca
            

            
                

    y_banana += velocidade
    if azul.colliderect(banana):
        x_banana = randint(10, 630)
        y_banana = 0
        pontos += 1
    if y_banana > altura:
        x_banana = randint(10, 630)
        y_banana = 0



    # if y_fruta > altura:
    #     y_fruta = 0
    #     x_fruta =  randint(10, 630)

    # for i in frutas_objetos:
    #     if azul.colliderect(i):
    #         if i == banana:
    #             y_banana = altura
    #         if i == maca:
    #             y_maca = altura
    #         if i == pera:
    #             y_pera = altura
    #         if i == caju:
    #             y_caju = altura
    #         if i == morango:
    #             y_morango = altura
    #     if i == banana:
    #             y_banana += velocidade
    #     if i == maca:
    #             y_maca += velocidade
    #     if i == pera:
    #             y_pera += velocidade
    #     if i == caju:
    #             y_caju += velocidade
    #     if i == morango:
    #             y_morango += velocidade
            


    # if azul.colliderect(verde):
    #     x_verde =  randint(40, 600)
    #     y_verde = randint(50, 430)
    #     som_colisao.play()
    #     pontos += 1 


    tela.blit(texto_formatado, (430, 40))
    pygame.display.update()

