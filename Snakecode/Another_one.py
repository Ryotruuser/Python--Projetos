import pygame
from random import randrange
from pygame.locals import *

pygame.init()
# cores

cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_red = (255, 0, 0)
cor_green = (0, 255, 0)
cor_blue = (0, 0, 255)
cor_rosa = (253,147,226)

# tamanho janela
larg = 640
alt = 480
tamanho = 10  # tamanho da snake
placar = 40


relogio = pygame.time.Clock()  # frame limiter

# display

fundo = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Jogo da cobrinha')


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam, bold=True)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def cobra(cobraxy):
    for xy in cobraxy:
        pygame.draw.rect(fundo, cor_green, [xy[0], xy[1], tamanho, tamanho])  # snake


def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, cor_red, [maca_x, maca_y, tamanho, tamanho])  # apple


def jogo():
    pygame.mixer.init()
    pygame.mixer.music.load('sons/bg.mp3')
    pygame.mixer.music.play(loops=-1)
    #  Posição Snake/ tamanho em pixels da snake/ velocidade da snake
    pos_x = randrange(0, larg - tamanho, 10)  # snake em paralelo spawnar em posição aleatoria *2
    pos_y = randrange(0, alt - tamanho - placar, 10)
    maca_x = randrange(0, larg - tamanho, 10)
    maca_y = randrange(0, alt - tamanho - placar, 10)
    velocidade_x = 0
    velocidade_y = 0
    sair = True
    fimdejogo = False
    CobraXY = []
    CobraComp = 1
    score = 0
    # Loop do game
    while sair:

        if fimdejogo:
            pygame.mixer.music.load('sons/fail.wav')
            pygame.mixer.music.play()

        # dando opções ao jogador fim de jogo e resete
        while fimdejogo:

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    sair = False
                    fimdejogo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_c:
                        pygame.mixer.init()
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sons/again.wav'), maxtime=2000)
                        pygame.mixer.music.load('sons/bg.mp3')
                        pygame.mixer.music.play(loops=-1)
                        pos_x = randrange(0, larg - tamanho, 10)  # snake em paralelo spawnar em posição aleatoria *2
                        pos_y = randrange(0, alt - tamanho - placar, 10)
                        maca_x = randrange(0, larg - tamanho, 10)
                        maca_y = randrange(0, alt - tamanho - placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        sair = True
                        fimdejogo = False
                        CobraXY = []
                        CobraComp = 1
                        score = 0
                    if evento.key == pygame.K_s:
                        sair = False
                        fimdejogo = False

            fundo.fill(cor_preta)
            texto('Fim de jogo', cor_green, 50, 210, 80)
            texto(f'Pontuação Final: {score}', cor_branca, 30, 210, 140)
            # botão 1
            pygame.draw.rect(fundo, cor_blue, [250, 190, 124, 27])
            texto('Continuar(C)', cor_branca, 25, 252, 197)
            # botão 2
            pygame.draw.rect(fundo, cor_red, [280, 227, 65, 27])
            texto('Sair(S)', cor_branca, 25, 280, 234)

            pygame.display.update()

        # frame limiter
        relogio.tick(27)

        # eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                sair = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = - tamanho

                if evento.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho

                if evento.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = - tamanho

                if evento.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

        if sair:  # não mostra a ultima visão do jogo ao sair
            # fundo.blit(fundotest, 0,0)
            fundo.fill(cor_preta)  # definiu uma cor para o fundo

            # ativar a snake
            pos_x += velocidade_x
            pos_y += velocidade_y

            # colisão maça
            if pos_x == maca_x and pos_y == maca_y:
                pygame.mixer.init()
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sons/bite.wav'), maxtime=2000)
                score += 10
                CobraComp += 5
                maca_x = randrange(0, larg - tamanho, 10)
                maca_y = randrange(0, alt - tamanho, 10)

            # bordas
            if pos_x + tamanho > larg:
                pos_x = 0
            if pos_x < 0:
                pos_x = larg - tamanho
            if pos_y + tamanho > alt:
                pos_y = 0
            if pos_y < 0:
                pos_y = alt - tamanho

            # logica da snake
            CobraInicio = [pos_x, pos_y]
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):  # Colisão da corpo da snake
                fimdejogo = True

            texto(f'Score: {score}', cor_rosa, 30, 10, alt - 30)

            cobra(CobraXY)
            maca(maca_x, maca_y)
            pygame.display.update()


jogo()
