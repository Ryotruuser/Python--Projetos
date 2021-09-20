
Pessoa = {'Nome':'Hugo', 'Profissao': 'Programador', 'Idade': '20'}

Pessoa['Nome'] = 'Renan'
print(Pessoa['Nome'])

class Pessoa():
    pass

x = Pessoa()

x.nome = 'Renan'
x.emprego = 'Proplayer'
x.idade = '21'

print(x.__dict__)