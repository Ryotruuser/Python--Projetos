#Codigo parcialmente correto acima de media print não funcionando em caso de 3 acimas da idade
#Resto do codigo funcionando perfeitamente
'''pep = dict()
pessoas = list()
wman = list()
old = list()
cont = 0
age = 0
idde = 0
c = 0
w = 0
while True:
    pep['nome'] = str(input('Nome: '))
    cont += 1
    pep['sexo'] = str(input('Sexo: [M/F] '))
    idade = pep['idade'] = int(input('Idade: '))
    age += idade
    resp = str(input('Quer continuar [S/N] '))
    pessoas.append(pep.copy())
    if resp in 'Nn':
        break
idde = age / cont
print('-=' * 30)
print(f'- O grupo tem {cont} pessoas.')
print(f'- A média de idade é de {idde} anos.')
for i, v in enumerate(pessoas):
    if pessoas[i]['sexo'] in 'Ff':
        wman.append(pessoas[i]['nome'])
        w += 1
for n in range(0, w):
    if n == 0:
        print(f'- As mulheres cadastradas foram: {wman[0]}', end=', ')
    else:
        print(wman[0 + 1], end='')
print()
for i, v in enumerate(pessoas):
    if pessoas[i]['idade'] > idde:
        old.append(pessoas[i]['nome'])
        old.append(pessoas[i]['idade'])
        old.append(pessoas[i]['sexo'])
        c += 1
print('- Lista das pessoas que estão acima da média:')
print()
for n in range(0, c):
    if n == 0:
        print(f'nome = {old[0]}; idade = {old[1]} sexo = {old[2]}')
        print()
    else:
        print(f'nome = {old[n + 2]}; idade = {old[n + 3]}; sexo = {old[n + 4]};')
        print()'''

#Resolução do professor
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')