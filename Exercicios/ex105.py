alunos = dict()
def notas(*num, sit=False):
    """
    -> Calcula media,maior e menor das notas de alunos e mostra situação(opcional)
    :param num: notas de alunos, quantas desejar
    :param sit: situação(opcional)
    :return: dicionario com varias informações sobre o sistema da turma
    """
    print()
    print('-' * 30)
    alunos['total'] = len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)
    alunos['media'] = sum(num) / len(num)
    if sit == True:
        if alunos['media'] >= 7:
            alunos['Situação'] = 'BOA'
        elif alunos['media'] > 5:
            alunos['Situação'] = 'RAZOAVEL'
        elif alunos['media'] < 5:
            alunos['Situação'] = 'RUIM'



notas(3.5,2,6.5,2,7,4,sit=True)
print(alunos)
