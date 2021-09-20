from time import sleep
from random import randint
print('\033[1;32m-=\033[m'*20 )
print('\033[1;35m    JOKENPOO!!! DOS MESTRES DA WEB\033[m')
print('\033[1;32m-=\033[m'*20)
print('''
\033[1;37m[0] PEDRA\033[m
\033[1;30m[1] PAPEL\033[m
\033[1;34m[2] TESOURA\033[m''')
jogador = int(input('\033[1;32mQual a sua jogada? \033[m'))
print('\033[1;33mJO!!!\033[m')
sleep(1)
print('\033[1;36mKEN!!!\033[m')
sleep(1)
print('\033[1;31mPOO!!!\033[m')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('\033[1;34mJogador jogou {} \033[m'.format(lista[jogador]))
print('\033[1;31mComputador jogou {} \033[m'.format(lista[computador]))
if jogador == 0:
    if computador == 2:
        print('\033[1;32mJogador Ganhou !!!\033[m')
    elif jogador == 0 and computador == 0:
        print('\033[1;33mEmpate!!!\033[m')
    else:
        print('\033[1;32mComputador Ganhou!!!\033[m')
if jogador == 1:
    if computador == 0:
        print('\033[1;32mJogador Ganhou!!!\033[m')
    elif jogador == 1 and computador == 1:
        print('\033[1;33mEmpate!!!\033[m')
    else:
        print('\033[32mComputador Ganhou!!!\033[m')
if jogador == 2:
    if computador == 1:
        print('\033[1;32mJogador Ganhou!!!\033[m')
    elif jogador == 2 and computador == 2:
        print('\033[1;33mEmpate!!!\033[m')
    else:
        print('\033[1;32mComputador Ganhou!!!\033[m')

