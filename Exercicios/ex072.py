num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte', 'Vinte um')
n = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
c = int(input('Digite um numero ente 0 e 20: '))
while True:
    if c not in n:
        c = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    else:
        print(f'Voce digitou o numero {num[c]}')
        break

