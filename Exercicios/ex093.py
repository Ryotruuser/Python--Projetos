'''tot = 0
q = 0
jogador = dict()
gols = list()
jogador['nome'] = str(input('Digite um nome: '))
c = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for n in range(0, c):
    q = (int(input(f'Quantos gols na partida {n + 1}? ')))
    gols.append(q)
    tot += q
jogador['gols'] = gols
jogador['total'] = tot
print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem o valor {jogador["nome"]}.')
print(f'O campo gols tem o valor {gols}.')
print(f'O campo total tem o valor {tot}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {c} partidas.')
for n in range(0, c):
    print(f'    => Na partida {n + 1}, fez {gols[n]} gols.')
print(f'Foi um total de {tot} gols.')'''

#Proposta de resposta do professor
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantras partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30 )
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')