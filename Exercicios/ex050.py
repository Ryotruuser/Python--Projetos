soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print('A soma dos {} numeros pares informados e igual a {}'.format(cont,soma))