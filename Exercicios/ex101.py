def voto(num):
    idade = 2019 - n
    if 18 < idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATORIO.')
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')
    if idade > 66:
        print(f'com {idade} anos: VOTO OPCIONAL.')

n = int(input('Ano de nascimento: '))
voto(n)