alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif alunos['média'] >= 5 < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in alunos.items():
    print(f'- {k} é igual {v}')

