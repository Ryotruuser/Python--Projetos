print('=============================')
print('         APPS FOR FUN')
print('=============================')
print('[0]Calcular '
      '[1]Multiplicar '
      '[2]Dividir '
      '[3]Tabuada '
      '[4]Sair')
a = int(input('Digite o numero correspondente a operação que deseja realizar:  '))
while a > 4:
    print('Operação inexistente, tente novamente.')
    a = int(input('Digite o numero correspondente a operação que deseja realizar:  '))
    if a == 0:
        a = int(input('1º Digito: '))
        b = int(input('2º Digito: '))
        c = a + b
        print(f'O resultado da sua soma entre {a} e {b} resulta no total de {c}')
    elif a == 1:
        a = int(input('1º Digito: '))
        b = int(input('2º Digito: '))
        c = a * b
        print(f'O resultado da multiplicação entre {a} e {b} resulta em {c}')
    elif a == 2:
        a = int(input('1º Digito: '))
        b = int(input('2º Digito: '))
        c = a / b
        print(f'O resultado da divisão entre {a} e {b} resulta em {c:1}')
    elif a == 3:
        a = int(input('Tabuada de qual valor: '))
        for i in range(0, 10):
            print(f'{a} x {i} = {a * i:2}')
    elif a == 4:
        print('Obrigado por usar nosso aplicativo, volte sempre.')
if a == 0:
    a = int(input('1º Digito: '))
    b = int(input('2º Digito: '))
    c = a + b
    print(f'O resultado da sua soma entre {a} e {b} resulta no total de {c}')
elif a == 1:
    a = int(input('1º Digito: '))
    b = int(input('2º Digito: '))
    c = a * b
    print(f'O resultado da multiplicação entre {a} e {b} resulta em {c}')
elif a == 2:
    a = int(input('1º Digito: '))
    b = int(input('2º Digito: '))
    c = a / b
    print(f'O resultado da divisão entre {a} e {b} resulta em {c:1}')
elif a == 3:
    a = int(input('Tabuada de qual valor: '))
    for i in range (0, 10):
        print(f'{a} x {i} = {a*i:2}')
elif a == 4:
    print('Obrigado por usar nosso aplicativo, volte sempre.')

