numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
if numero1 > numero2:
    print('O PRIMEIRO numero e maior')
elif numero2 > numero1:
    print('O SEGUNDO numero e maior')
elif numero1 == numero2:
    print('Os numeros são iguais')
else:
    print('Erro, tente novamente.')
