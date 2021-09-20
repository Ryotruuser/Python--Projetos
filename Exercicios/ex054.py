from datetime import date
cont2 = 0
cont = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(c)))
    idade = atual - ano
    if idade >= 21:
        cont += 1
    elif idade < 21:
        cont2 += 1
print('Ao todo tivemos {} pessoas maiores'.format(cont))
print('e tambem tivemos {} menores'.format(cont2))
