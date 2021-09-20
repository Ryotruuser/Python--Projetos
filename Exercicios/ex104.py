def leiaint(numero=0):
    while True:
        n = str(input(numero))
        conf = str.isdigit(n)
        if conf == False:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return n
            break

n = leiaint('digite um numero: ')
print(f'Você digitou o número {n}')