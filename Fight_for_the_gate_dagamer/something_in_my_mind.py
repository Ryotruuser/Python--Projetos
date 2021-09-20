""""
FDS
REFINAR COLISÃO
MAIS INIMIGOS
INIMIGOS PODEM GANHAR
"""

import pygame, sys
from random import randint
from pygame.locals import *



larg = 900
alt = 400



class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Imagem2 = pygame.image.load('imagens/enemy2.png')
        self.Imagemalien = self.Imagem2

        self.rect = self.Imagemalien.get_rect()
        self.rect.centerx = 450
        self.rect.centery = 50


        self.life = True
        if self.life == False:
            return
        centerx = self.rect.centerx
        centery = self.rect.centery


    def colocar(self, superficie):
        self.Imagemalien = self.Imagem2
        superficie.blit(self.Imagemalien, self.rect)

    def Mudar(self,superficie):
        self.Imagemalien = self.Imagem2
        superficie.blit(self.Imagemalien,self.rect)
        self.rect.centery = randint(50, 120)
        self.rect.centerx = randint(20, 800)


class Bala3(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('imagens/green.png')

        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 9
        self.rect.top = posy
        self.rect.left = posx

    def trajeto(self):
        self.rect.top = self.rect.top - self.velocidadeBala

    def colocar(self, superficie):
        superficie.blit(self.ImagemBala, self.rect)

class Bala2(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('imagens/yellow.png')

        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 9
        self.rect.top = posy
        self.rect.left = posx

    def trajeto(self):
        self.rect.top = self.rect.top + self.velocidadeBala

    def colocar(self, superficie):
        superficie.blit(self.ImagemBala, self.rect)

class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('imagens/orange.png')

        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 9
        self.rect.top = posy
        self.rect.left = posx

    def trajeto(self):
        self.rect.top = self.rect.top - self.velocidadeBala

    def colocar(self, superficie):
        superficie.blit(self.ImagemBala, self.rect)

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave= pygame.image.load('imagens/nave.png')

        self.rect = self.ImagemNave.get_rect() # pega minha imagem e coloca ela em retangular
        self.rect.centerx = larg / 2
        self.rect.centery = alt - 50

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 60



    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()

    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0

            elif self.rect.right > 900:
                self.rect.right = 900

    def disparar(self, x,y):
        minhaBala = Bala(x,y)
        self.listaDisparo.append(minhaBala)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sons/1.wav'), maxtime= 2000)

    def disparar2(self, x,y):
        minhaBala2 = Bala2(x,y)
        self.listaDisparo.append(minhaBala2)


    def disparar3(self, x,y):
        minhaBala3 = Bala3(x,y)
        self.listaDisparo.append(minhaBala3)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sons/1.wav'), maxtime= 2000)



    def colocar(self, superficie):
        superficie.blit(self.ImagemNave, self.rect)


def invasaoEspaco():
    pygame.init()
    pygame.mixer.init()
    tela = pygame.display.set_mode((larg, alt))
    icone = pygame.image.load('Folder.jpg')
    pygame.display.set_icon(icone)
    pygame.display.set_caption('Fight For The Gate')
    jogador = NaveEspacial()
    imagemFundo = pygame.image.load('imagens/fundo.jpg')
    font_padrao = pygame.font.get_default_font()
    fonte_hit = pygame.font.SysFont(font_padrao, 32)
    fonte_score = pygame.font.SysFont(font_padrao, 40)
    jogando = True
    score = 0
    balaProjetil = Bala(larg / 2, alt - 60)
    fps = pygame.time.Clock()
    pygame.Rect(balaProjetil)
    inimigo = Alien()
    bala = jogador.listaDisparo
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sons/bg.mp3')
    pygame.mixer.music.play(loops=-1)


    while True:


        fps.tick(57)
        balaProjetil.trajeto()




        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit() # quite toda aplicação rodando para evitar erros


            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jogador.movimentoEsquerda()

                if evento.key == K_RIGHT:
                    jogador.movimentoDireita()

                elif evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    z,v = inimigo.rect.center
                    a,b = jogador.rect.center
                    jogador.disparar(x - 20, y)
                    jogador.disparar3(x + 20, y)
                    jogador.disparar2(z - 2, 100 )




        tela.blit(imagemFundo, (0,0))
        inimigo.colocar(tela)
        inimigo.colocar(tela)
        jogador.colocar(tela)






        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajeto()
                if x.rect.top < -10:
                    jogador.listaDisparo.remove(x)
                if x.rect.colliderect(inimigo):
                    inimigo.Mudar(tela)
                    score += 2
                    text = fonte_hit.render('+ 2', 1, (120,235,230))
                    tela.blit(text, (70,20))



        placar = fonte_score.render(f'Score: {score}', 1, (124, 65, 197))
        tela.blit(placar, (0, 0))


        pygame.display.update()

invasaoEspaco()
