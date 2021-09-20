'''anotual = 2019
dado = dict()
dado['nome'] = str(input('Nome: '))
dado['nasc'] = int(input('Ano de nascimento: '))
dado['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
idade = anotual - dado['nasc']
if dado['ctps'] > 0:
    dado['contrato'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salario: R$ '))
    aps = (dado['contrato'] - dado['nasc']) + 35
    print('-=' * 30)
    print(f'Nome tem valor {dado["nome"]}')
    print(f'Idade tem valor {idade}')
    print(f'Ctps tem valor {dado["ctps"]}')
    print(f'Contratação tem valor {dado["contrato"]}')
    print(f'Salário tem valor {dado["salario"]}')
    print(f'Aposentadoria tem valor {aps}')
else:
    print('-=' * 30)
    print(f'Nome tem valor {dado["nome"]}')
    print(f'Idade tem valor {idade}')
    print(f'Ctps tem valor {dado["ctps"]}')'''

#Solução proposta pelo professor, abaixo.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')