'''
try:
    x = int(input('Digite um numero: '))
    print(x)
except:
    print('Deu erro, insira apenas numeros')

finally:
    print('Independete de erro')
'''

class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n

    def __str__(self):
         return f'Vixe! Você ja digitou o valor {self.num} antes'

def main():
    lista = []
    for i in range(8):
        while True:
            try:
                num = int(input('Digite um numero: '))
                break
            except ValueError:  # trata erros
                print('Digite apenas numeros')

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num) # chama minha classe

main()