import pygame
import time
from random import randint
from configuracoes import *
import math


class Fruta(pygame.sprite.Sprite):
    def __init__(self, url, tipoFruta , nome):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(url) 
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,LARGURA-50)
        self.rect.y = 0 - 50
        self.velocidade = 5
        self.mask = pygame.mask.from_surface(self.image)
        self.tipoFruta = tipoFruta
        self.nome = nome
    def update(self):
        self.rect.y += self.velocidade   


class Especial(pygame.sprite.Sprite):
    def __init__(self, url , tipoEspecial):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(url)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,LARGURA-50)
        self.rect.y = 0 - 50
        self.VELOCIDADE = VELOCIDADE_ESPECIAL
        self.mask = pygame.mask.from_surface(self.image)
        self.tipoEspecial = tipoEspecial
    def update(self):
        self.rect.y += self.VELOCIDADE
    

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagensPersonagem = []
        img = SPRITESHEET_PERSONAGEM.subsurface((0, 0), (66.75, 100))
        self.imagensPersonagem.append(img)
        for i in range(4):
            img = SPRITESHEET_PERSONAGEM.subsurface((i * 66.75, 200), (66.75, 100))
            self.imagensPersonagem.append(img)
        for i in range(4):
            img = SPRITESHEET_PERSONAGEM.subsurface((i * 66.75, 300), (66.75, 100))
            self.imagensPersonagem.append(img)
        self.atual = 0
        self.image = self.imagensPersonagem[self.atual]
        self.rect = self.image.get_rect()
        self.rect.x = LARGURA/2 - 66.75
        self.rect.y = ALTURA*0.85
        self.velocidade = 11
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if(pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.x > 0):
            self.rect.x -= self.velocidade
            if(self.atual > 4 or self.atual == 0):
                self.atual = 1
            self.atual += 0.25
            self.image = self.imagensPersonagem[int(self.atual)]
        else:
            self.image = self.imagensPersonagem[0]
        if(pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]) and self.rect.x < LARGURA - 66.75:
            self.rect.x += self.velocidade
            if(self.atual < 5 or self.atual > 8):
                self.atual = 5
            self.atual += 0.25
            self.image = self.imagensPersonagem[int(self.atual)]
        

class Jogo:
    def __init__(self):
        pygame.init()
        # pygame.mixer.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JOGO)
        self.fonte = pygame.font.match_font(FONTE)
        self.relogio = pygame.time.Clock()
        self.rodando = True

    def novo_jogo(self):
        #Instancia as variáveis do jogo
        self.frutasConsumidas = {
            'abacaxiBatizado': 0,
            'uvaBatizada': 0,
            'morangoBatizado': 0,
            'bananaBatizada': 0,
            'macaBatizada': 0,

            'abacaxi': 0,
            'morango': 0,
            'uva': 0,
            'banana': 0,
            'maca': 0
        }

        self.grupoFrutas = pygame.sprite.Group()
        self.grupoPersonagens = pygame.sprite.Group()
        self.grupoEspeciais = pygame.sprite.Group()

        self.largura_saude = 120
        self.largura_vida = 120
        self.largura_turbo = 300

        self.personagem = Personagem()
        self.grupoPersonagens.add(self.personagem)

        self.tempoFrutaRuim = []
        self.perderSaude = False

        self.jogando = True
        
        self.rodar()

    def rodar(self):
        #Loop do jogo
        tempo_dificultar = int(time.time())
        tempo_fruta = int(time.time())
        tempo_inicial_especial = int(time.time())
        segundos_fruta = 3

        while self.jogando:
            self.relogio.tick(FPS)
            self.tela.blit(FUNDO, (0,0))
            self.eventos()
            self.desenhar_e_atualizar_sprites()
            self.mostrar_texto(f'{int(self.largura_saude)}', 10, PRETO, 9, 24)
            self.mostrar_texto(f'{int(self.largura_vida)}', 10, PRETO, 9, 39)
            self.mostrar_texto(f'{int(self.largura_turbo)}', 10, PRETO, 9, 9)
            self.colisoes()
            
            tempo_loop = int(time.time())
            if self.largura_saude > 80:
                self.personagem.velocidade = 11
            elif self.largura_saude > 60:
                self.personagem.velocidade = 9
            elif self.largura_saude > 40:    
                self.personagem.velocidade = 8
            elif self.largura_saude > 20:
                self.personagem.velocidade = 7
            elif self.largura_saude > 0:
                self.personagem.velocidade = 6
            
            
            if pygame.key.get_pressed()[pygame.K_SPACE] and  self.largura_turbo > 0:
                if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]) and self.personagem.rect.x > 0:
                    self.personagem.rect.x -= 3
                    self.largura_turbo -= 1
                if (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]) and self.personagem.rect.x < LARGURA - 66.75:
                    self.personagem.rect.x += 3
                    self.largura_turbo -= 1
            
            barraDeSaude = pygame.draw.rect(self.tela, AZUL, (X_BARRA_SAUDE, Y_BARRA_SAUDE, math.ceil(self.largura_saude), ALTURA_SAUDE))
            barraDeVida = pygame.draw.rect(self.tela, VERMELHO, (X_BARRA_VIDA, Y_BARRA_VIDA, math.ceil(self.largura_vida), ALTURA_VIDA))   
            barraDeTurbo = pygame.draw.rect(self.tela, PRETO, (X_BARRA_TURBO, Y_BARRA_TURBO, self.largura_turbo, ALTURA_TURBO))

            if(int(tempo_loop - tempo_dificultar) >= 5 and segundos_fruta > 1):
                segundos_fruta -= 0.5
                tempo_dificultar = int(time.time())

            if(tempo_loop - tempo_fruta >= segundos_fruta):
                tempo_fruta = tempo_loop
                fruta = self.criar_fruta()
                self.grupoFrutas.add(fruta)

            if tempo_loop - tempo_inicial_especial >= SEGUNDOS_ESPECIAL:
                tempo_inicial_especial = tempo_loop
                especial = self.sorteia_especial()
                self.grupoEspeciais.add(especial)

            if(self.perderSaude == True and self.largura_saude > 0):
                self.largura_saude -= 0.1

            if(self.largura_saude <= 0 and self.largura_vida > 0):
                self.largura_vida -= 0.2
    
            tamanho = len(self.tempoFrutaRuim)
            if(tamanho != 0):     
                if(time.time() - self.tempoFrutaRuim[0] >= 5*tamanho):
                    self.perderSaude = False
                    self.tempoFrutaRuim = []

            for fruta in self.grupoFrutas:
                if(fruta.rect.y >= ALTURA+20):
                    self.grupoFrutas.remove(fruta)
                    if(not "Batizado" in fruta.tipoFruta and not "Batizada" in fruta.tipoFruta):
                        if(self.largura_saude - 10 < 0):
                            self.largura_saude -= self.largura_saude
                        else:
                            self.largura_saude -= 10
            
            if(int(self.largura_vida) == 0):
                self.jogando = False
          
            pygame.display.flip()
    
    def colisoes(self):
        colisaoFrutas = pygame.sprite.spritecollide(self.personagem, self.grupoFrutas, True, pygame.sprite.collide_mask)
        if(colisaoFrutas): 
            if("Batizado" in colisaoFrutas[0].tipoFruta or "Batizada" in colisaoFrutas[0].tipoFruta):
                self.perderSaude = True
                self.tempoFrutaRuim.append(time.time())
            else:
                if((self.largura_saude+1) <= 120):
                    self.largura_saude += 1
            self.frutasConsumidas[colisaoFrutas[0].tipoFruta] += 1

        colisaoEspeciais = pygame.sprite.spritecollide(self.personagem, self.grupoEspeciais, True, pygame.sprite.collide_mask)
        if colisaoEspeciais:
            if colisaoEspeciais[0].tipoEspecial == "Especial01":
                #azul
                self.largura_saude += 30
            if colisaoEspeciais[0].tipoEspecial == "Especial02":
                #dourado
                for fruta in self.grupoFrutas:
                    fruta = self.especialDourado(fruta)
    
    def criar_fruta(self):
        tipo = randint(0, 9)
        match tipo:
            case 0:
                return Fruta(f"./sprites/banana/banana.png", "banana", "banana")
            case 1:
                return Fruta("./sprites/banana/bananaBatizada.png" , "bananaBatizada", "banana")
            case 2:
                return Fruta("./sprites/maca/maca.png", 'maca', 'maca')
            case 3:
                return Fruta("./sprites/maca/macaBatizada.png" , "macaBatizada", "maca")
            case 4:
                return Fruta("./sprites/uva/uva.png", "uva", "uva")
            case 5:
                return Fruta("./sprites/uva/uvaBatizada.png", "uvaBatizada", "uva")
            case 6:
                return Fruta("./sprites/morango/morango.png", "morango", "morango")
            case 7:
                return Fruta("./sprites/morango/morangoBatizado.png", "morangoBatizado", "morango")
            case 8:
                return Fruta("./sprites/abacaxi/abacaxi.png", "abacaxi", "abacaxi")
            case 9:
                return Fruta("./sprites/abacaxi/abacaxiBatizado.png", "abacaxiBatizado", "abacaxi")
            
    def especialDourado(self, objeto):
        nomeFruta = objeto.nome
        objeto.image = pygame.image.load(f"./sprites/{nomeFruta}/{nomeFruta}.png")
        objeto.tipoFruta = nomeFruta
        return objeto   
        
    def sorteia_especial(self):
        sorteio = randint(0, 1)
        match(sorteio):
            case 0:
                return Especial("./sprites/especiais/especial_01.png", "Especial01")
            case 1:
                return Especial("./sprites/especiais/especial_02.png", "Especial02")
    
    def eventos(self):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def desenhar_e_atualizar_sprites(self):
        self.tela.blit(FUNDO, (0,0))
        self.grupoEspeciais.draw(self.tela)
        self.grupoFrutas.draw(self.tela)
        self.grupoPersonagens.draw(self.tela)
        self.grupoEspeciais.update()
        self.grupoFrutas.update()
        self.grupoPersonagens.update()
    
    def mostrar_texto(self, texto, tamanho, cor, x, y):
        #Exibe um texto na tela
        fonte = pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(texto, True, cor)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.midtop = (x, y)
        self.tela.blit(mensagem, mensagem_rect)   

    def mostrar_tela_start(self):
        self.tela.blit(FUNDO, (0,0))
        self.mostrar_texto('-Pressione a tecla "G" para jogar-', 40, BRANCO, LARGURA/2, ALTURA*0.85)
        self.mostrar_texto('Desenvolvido por Igor Nara, Pedro Schuenck e Matheus Stutz', 30, BRANCO, LARGURA/2, ALTURA*0.95)
        pygame.display.flip()
        self.esperar_start()
    
    def esperar_start(self):
        esperando = True
        while esperando:
            self.relogio.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        esperando = False

    def mostrar_tela_game_over(self):
        self.tela.blit(GAME_OVER, (0,0))
        self.mostrar_texto('-Pressione a tecla "R" para voltar à tela inicial-', 30, PRETO, LARGURA/2, ALTURA/5)
        self.mostrar_texto('-Pressione a tecla "C" para fechar o jogo-', 30, PRETO, LARGURA/2, ALTURA/4)
        porcentagemX = 0.11
        porcentagemY = 0.23
        contador = 1
        for frutaConsumida in self.frutasConsumidas.items():
            if("Batizado" in frutaConsumida[0] or "Batizada" in frutaConsumida[0]):
                self.mostrar_texto(f'{frutaConsumida[1]}', 40, PRETO, LARGURA*porcentagemX, ALTURA*porcentagemY)
                if(contador  == 3):
                    porcentagemX = 0.11
                    porcentagemY += 0.11
                else:
                    porcentagemX += 0.08
                contador += 1

        porcentagemX = 0.74
        porcentagemY = 0.23
        contador = 1
        for frutaConsumida in self.frutasConsumidas.items():
            if(not "Batizado" in frutaConsumida[0] and not "Batizada" in frutaConsumida[0]):
                self.mostrar_texto(f'{frutaConsumida[1]}', 40, PRETO, LARGURA*porcentagemX, ALTURA*porcentagemY)
                if(contador  == 3):
                    porcentagemX = 0.81
                    porcentagemY += 0.10
                else:
                    porcentagemX += 0.07
                contador += 1

        pygame.display.flip()
        self.esperando_restart()
        
    def esperando_restart(self):
        esperando = True
        while esperando:
            self.relogio.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.rodando = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        esperando = False
                    if event.key == pygame.K_c:
                        esperando = False
                        self.rodando = False
                    
                    
            pygame.display.flip()

jogo = Jogo()

while jogo.rodando:
    jogo.mostrar_tela_start()
    jogo.novo_jogo()
    jogo.mostrar_tela_game_over()
