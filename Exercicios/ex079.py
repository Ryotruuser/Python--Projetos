lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, tente novamente.')
    fse = str(input('Quer continuar [S/N] ')).upper().strip()
    if fse in 'Nn':
        break


lista.sort()
print(f'Você digitou os valores {lista}')