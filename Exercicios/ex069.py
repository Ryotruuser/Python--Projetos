cont = idade = genero = men = wom = 0
while True:
    print('-=' * 15)
    print('     CADASTE UMA PESSOA')
    print('-=' * 15)
    idade = int(input('Qual sua idade: '))
    genero = str(input('Qual seu genero: ')).upper()
    while genero != 'F' and genero != 'M':
        genero = str(input('Qual seu genero: ')).upper()
    fim = str(input('Quer continuar? [S/N] ')).upper()
    while fim != 'S' and fim != 'N':
            fim = str(input('Quer continuar? [S/N] ')).upper()
    if genero == 'F' and idade < 20:
        wom += 1
    if genero == 'M':
        men += 1
    if idade > 18:
        cont += 1
    if fim == 'N':
        break
print('=-'*25)
print(f'{cont} Pessoas maiores de 18 anos.')
print(f'{men} Homens foram cadastrados.')
print(f'{wom} Mulheres com menos de 20 anos foram cadastradas.')
print('=-'*25)
