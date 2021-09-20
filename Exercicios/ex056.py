# Analisador
cont = 0
men = 0
wman = 0
male = 0
fmale = 0
nomereal = 0
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    genero = str(input('Sexo [M/F]: ')).upper()
    cont += idade
    mediai = cont / p
    if genero == 'F' and idade < 20:
        wman = wman + 1
        fmale += 1
    elif genero == 'M':
        male += 1
        var = men == idade
        var = nomereal == nome
        if idade > men:
            men = idade
            nomereal = nome
print(' '*50)
print('A média de idade do grupo e de {:.1f} anos'.format(mediai))
if male > 0:
    print('O Homem mas velho do grupo tem {} anos e se chama {}'.format(men, nomereal))
if fmale > 0:
    print('Temos apenas {} mulher com menos de 20 anos '.format(wman))
elif fmale > 2:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(wman))
