'''def test():
    livro = list()
    pessoa = dict()
    def cadastro():
        print('-' * 30)
        pessoa['nome'] = str(input('Qual seu nome: ')).upper()
        pessoa['idade'] = int(input('Qual seu idade: '))
        pessoa['sexo'] = str(input('Qual seu gênero [M/F]: ')).upper()[0]
        pessoa['nasc'] = 2018 - pessoa['idade']
        livro.append(pessoa.copy())
    c = int(input('Quantas pessoas quer cadastrar: '))
    for n in range(1, c + 1):
        cadastro()
    for i, v in enumerate(livro):
        print(f'{v["nome"]} foi cadastrado com sucesso, Gênero {v["sexo"]}, nascido em {v["nasc"]}.')'''
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 3)
soma(2, 9, 4)