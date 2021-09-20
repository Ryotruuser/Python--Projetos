#Minha solução

matr = [[], [], []]
valor = 0
for c in range(0, 3):
    matr[0].append(int(input(f'Digite um valor para [{0, c}]')))
for c in range(0, 3):
    matr[1].append(int(input(f'Digite um valor para [{1, c}]')))
for c in range(0, 3):
    matr[2].append(int(input(f'Digite um valor para [{2, c}]')))
print('-=' * 30)
print(f'[{matr[0][0]:^5}] [{matr[0][1]:^5}] [{matr[0][2]:^5}]')
print(f'[{matr[1][0]:^5}] [{matr[1][1]:^5}] [{matr[1][2]:^5}]')
print(f'[{matr[2][0]:^5}] [{matr[2][1]:^5}] [{matr[2][2]:^5}]')

#Resposta proposta pelo professor

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''