n = cont = soma = media = maior = menor = 0
while n != 1:
    numero = int(input('Digite  um número: '))
    n = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if n == 'S':
        n = 0
    if n == 'N':
        n = 1
media = soma / cont
print('Você digitou {} e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
