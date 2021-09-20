temp = []
alunos = []
fim = media = cont = 0
while True:
    nome = str(input('Nome: '))
    cont += 1
    temp.append(nome)
    nota1 = float(input('Nota 1: '))
    temp.append(nota1)
    nota2 = float(input('Nota 2: '))
    temp.append(nota2)
    media = (nota1 + nota2) / 2
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 20)
print('No. {:<7}{:>20}'.format('NOME', 'MÉDIA'))
print('-' * 33)
for c in range(0, cont):
    print(f'{c}   {alunos[c][c - c]:<20}', end='    ')
    print(f'{alunos[c][(c - c) + 3]:<7}', end='   ')
    print()
print('-' * 33)
while fim != 999:
    fim = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for i, n in enumerate(alunos):
        if fim == i:
            print(f'Notas de {alunos[i][0]} são [{alunos[i][1]}, {alunos[i][2]}]')

#Proposta de resposta pelo professor
'''ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2 ) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')'''

