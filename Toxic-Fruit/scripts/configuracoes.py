import pygame
import os

pygame.init()

caminhoAtual = os.getcwd()

screen_info = pygame.display.Info()

LARGURA = screen_info.current_w
ALTURA = screen_info.current_h

FUNDO = pygame.image.load(f'{caminhoAtual}/telas/fundo.png')
FUNDO = pygame.transform.scale(FUNDO, (LARGURA, ALTURA))
GAME_OVER = pygame.image.load(f'{caminhoAtual}/telas/game-over.png')
GAME_OVER = pygame.transform.scale(GAME_OVER, (LARGURA, ALTURA))

TITULO_JOGO = 'Toxic-Fruit'

FPS = 75

FONTE = 'arial'

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

X_BARRA_SAUDE = 20
Y_BARRA_SAUDE = 25
ALTURA_SAUDE = 10

X_BARRA_VIDA = 20
Y_BARRA_VIDA = 40
ALTURA_VIDA = 10

X_BARRA_TURBO = 20
Y_BARRA_TURBO = 10
ALTURA_TURBO = 10

SEGUNDOS_ESPECIAL = 30
VELOCIDADE_ESPECIAL = 4

SPRITESHEET_PERSONAGEM = pygame.image.load(f"sprites/personagem/spritesPersonagem.png")