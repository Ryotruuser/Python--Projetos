numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das opções abaixo para conversão
[1] converter para BÍNARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} em BÍNARIO e {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} em OCTAL fica {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} em HEXADECIMAL e igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção incorreta, tente novamente.')
