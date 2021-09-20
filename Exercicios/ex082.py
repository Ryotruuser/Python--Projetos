lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
        print('Numero par adicionado com sucesso...')
    else:
        impar.append(n)
        print('Numero impar adicionado com sucesso...')
    r = str(input('Quer continuar [S/N] '))
    if r in 'nN':
        break
lista.sort()
print('-=' * 30)
print(f'Aqui está sua lista {lista}')
print(f'Esses foram os numeros pares encontrados {par}')
print(f'E esses os numeros immpares {impar}')


''' Solução Proposta pelo professor
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um valor:)))
    resp = str(input('Quer continuar [S/N] ))
    if resp in 'Nn' 
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
# na linha for 'i' refere-se a index e 'v' refere-se a valor.
'''