primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razao #Calculo do decimo termo de uma PA
for c in range(primeiro, décimo + razao, razao):
    print('{} '.format(c), end='» ')
print('ACABOU ')