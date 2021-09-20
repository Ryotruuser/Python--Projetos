from time import sleep
n = 0
r = 0
nw = 0
nw1 = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while n != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa''')
    n = int(input('>>>>> Qual é a sua opção? '))
    if n == 1:
        r = n1 + n2
        print('A soma entre {} e {} e igual a {}'.format(n1, n2, r))
    if n == 2:
        r = n1 * n2
        print('{} X {} tem resultado igual a {}'.format(n1, n2, r))
    if n == 3:
        if n1 > n2:
            print('O numero {} e maior'.format(n1))
        elif n2 > n1:
            print('O numero {} e maior'.format(n2))
        else:
            print('Os numeros São equivalentes, logo não existe maior.')
    if n == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if n == 5:
        sleep(1)
        print('Finalizando...')
    if n != 1 and n != 2 and n != 3 and n != 4 and n != 5:
        print('Opção invalida, digite uma opção valida.')
