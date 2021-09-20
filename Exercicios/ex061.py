print('='* 21)
print('Progressão Aritmetica')
print('='* 21)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
termo = primeiro
while cont != 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
