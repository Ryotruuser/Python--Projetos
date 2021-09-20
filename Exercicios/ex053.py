#A frase e um palindromo ? ou seja ana que de tras pra frente e a mesma palavra.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#Sem a estrutura de repetição for. Mas simples e limpo
inverso = junto[::-1]
#Com a estrutua de repetição for
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não e um palíndromo!')