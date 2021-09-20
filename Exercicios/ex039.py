ano = int(input('ano de nascimento: '))
idade = 2018 - ano
tempo = 18 - idade
print('Quem nasceu em {} tem {} anos em 2018'.format(ano, idade))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(tempo))
elif idade == 18:
    print('Aliste-se imediatamente !!!')
elif idade > 18:
    print('Você está atrasado seu alistamento foi em {}'.format(ano + 18))

