br = ('Zero','Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo', 'Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','America-MG','Vitoria','Paraná')
print(br)
print('=' * 50)
print('{:^50}'.format('Cinco primeiros Colocados'))
print('=' * 50)
print(br[1:6])
print('=' * 50)
print('{:^50}'.format('Quatro Ultimos'))
print('=' * 50)
print(br[-4:])
print('=' * 50)
print('{:^50}'.format('Ordem alfabetica'))
print('=' * 50)
print(sorted(br[1:20]))
print('=' * 50)
print('{:^50}'.format('Chape'))
print('=' * 50)
print('A Chapecoense está na', br.index('Chapecoense'),'posição')
