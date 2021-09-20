def ficha(nome='', gol=0):
    if len(gol) == 0:
        gol = int
        gol = 0
    if len(nome) == 0:
        nome = '<Desconhecido>'
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


print('-' * 20)
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

ficha(n, g)
