'''dado = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    cont = int(input(f'  Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, cont):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    gols.clear()
    dado.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('Cod nome    gols        total')
print('-' * 30)
for i, v in enumerate(dado):
    print(f'{i} {v["nome"]}    {v["gols"]}        {sum(v["gols"])}')
print('-' * 30)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print(f' -- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
    for i, v in enumerate(jogador['gols']):
        if n == 0:
            print(f'    No jogo {i + 1} fez {v} gols.')
        if n > 0:
            print(f'    No jogo {i + 1} fez {v} gols.')
    print('-' * 30)
    if n == 999:
        break
print(jogador)'''

#solução do professorg
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantras partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')