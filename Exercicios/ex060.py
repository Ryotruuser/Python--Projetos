from math import factorial
n = 0
a = 0
while n != 1:
    n = int(input('''Digite um numero para
calcular seu Fatorial: '''))
    print('O fatorial de {} e {}'.format(n,factorial(n)))
    a = str(input(('Continue ? [S/N] '))).upper()
    if a == 'S':
        n = 0
    else:
        n = 1