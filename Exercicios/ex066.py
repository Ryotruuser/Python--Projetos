numero = soma = numeros = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    numeros += 1
    if numero == 999:
        numeros -= 1
        break
    soma += numero
print(f'Você digitou {numeros} numeros a soma todos eles e de {soma}')