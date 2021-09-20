num = int(input('Digite um numero: '))
num1 = int(input('Digite outro numero: '))
num2 = int(input('Digite mais um numero: '))
num3 = int(input('Digite o ultimo numero: '))
t = num, num1, num2, num3
cont = 0
print(f'Os valores digitados foram {num, num1, num2, num3}')
print('O valor 9 apareceu',t.count(9),'vezes')
if 3 in t:
    print('O valor 3 apareceu na',t.index(3),'posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Valores pares digitados', end=' ')
if num % 2 == 0:
    print(num, end=' ')
else:
    cont += 1
if num1 % 2 == 0:
    print(num1, end=' ')
else:
    cont += 1
if num2 %  2 == 0:
    print(num2, end=' ')
else:
    cont += 1
if num3 % 2 == 0:
    print(num3, end=' ')
else:
    cont += 1
if cont >= 4:
    print('Nenhum valor par digitado')
