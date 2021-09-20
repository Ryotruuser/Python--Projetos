temp = []
pessoas = []
mai = men = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        mai = men = 0
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{len(pessoas)} Pessoas foram cadastradas')
print(f'O maior peso foi de {mai}Kg', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {min(pessoas)}Kg', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()