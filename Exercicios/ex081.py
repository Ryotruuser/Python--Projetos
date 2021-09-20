lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n)
    r = str(input('Quer continuar [S/N] '))
    if r in 'nN':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista !')
else:
    print('O valor 5 não foi encontrado na lista!')