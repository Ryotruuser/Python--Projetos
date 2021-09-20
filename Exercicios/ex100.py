from random import randint
numero = []
temp = []

def sorteia(lista):
    print(f'Sorteando 5 valores da lista:',end=' ')
    for n in range(1,6):
        pc = randint(0, 10)
        print(pc, end=' ')
        lista.append(pc)
    print('PRONTO!')


def somapar(lista):
    cont = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            cont += v
    print(f'Somando os valores pares de {lista}, temos {cont}')

sorteia(numero)
somapar(numero)