cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} numeros impares multiplos de 3 e igual a {}'.format(cont,soma))
