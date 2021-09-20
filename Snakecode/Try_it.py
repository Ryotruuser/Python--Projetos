import pygame
import sys
from random import randrange

larg = 640
alt = 480
#Cores
cor_branca = (255,255,255)
cor_azul = (108,194,236)
cor_verde = (152,231,114)
red_color = (227,59,9)
cor_rosa = (253,147,226)
cor_preta = (0,0,0)
tela = pygame.display.set_mode([larg,alt])
pygame.display.set_caption('Estudando pygame')
tamanho = 10


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam, bold=True)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])

def maca(maca_x, maca_y):
    pygame.draw.rect(tela, cor_branca, [maca_x, maca_y, tamanho, tamanho])  # apple



def cobra(cobraxy):
    for xy in cobraxy:
        pygame.draw.rect(tela, cor_verde, [xy[0], xy[1], tamanho, tamanho])  # snake



def main():
    pygame.init()
    #As definições dos objetos(variaveis)
    relogio = pygame.time.Clock()
    pos_x = randrange(0, larg - tamanho, 10)  # snake em paralelo spawnar em posição aleatoria *2
    pos_y = randrange(0, alt - tamanho  , 10)
    maca_x = randrange(0, larg - tamanho, 10)
    maca_y = randrange(0, alt - tamanho , 10)
    CobraXY = []
    CobraComp = 1
    velocidade_x = 0
    velocidade_y = 0
    score = 0

    #situation
    sair = False

    while sair != True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
                pygame.quit()
                sys.exit()
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

        if pos_x + tamanho > larg:
            pos_x = 0
        if pos_x < 0:
            pos_x = larg - tamanho
        if pos_y + tamanho > alt:
            pos_y = 0
        if pos_y < 0:
            pos_y = alt - tamanho

        if pos_x == maca_x and pos_y == maca_y:
            pygame.mixer.init()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sons/bite.wav'), maxtime=2000)
            score += 10
            CobraComp += 5
            maca_x = randrange(0, larg - tamanho, 10)
            maca_y = randrange(0, alt - tamanho, 10)



        CobraInicio = [pos_x, pos_y]
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):  # Colisão da corpo da snake
            pass

        pos_x += velocidade_x
        pos_y += velocidade_y


        relogio.tick(27)
        tela.fill(cor_preta)

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


main()

