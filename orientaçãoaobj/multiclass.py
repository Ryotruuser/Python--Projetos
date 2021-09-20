class Animal:
    def __init__(anim, cor, genero, patas):
        anim.cor = cor
        anim.genero = genero
        anim.patas = patas

    def falar(anim):
        if anim.genero == 'Masculino':
            print('Olá sou um cachorro e sei falar')
        if anim.genero == 'Feminino':
            print('Sou uma cadela e sei falar')


    def andar(anim):
        print(f'Estou andando sobre {anim.patas} patas')

    def amamentar(anim):
        if anim.genero.lower() [0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentando meu filhote')

'''
Rex = Animal('marrom','macho', 4)
Rex.falar()
Rex.andar()
Rex.amamentar()
'''

class Pessoa(Animal):
    def __init__(anim, cor, genero, patas, cabelo):
        super(Pessoa, anim).__init__(cor, genero, patas) # linkando parametros da class Pessoa para essa
        anim.cabelo = 'Castanho'

    def falar(anim):
        super(Pessoa, anim).falar()
        print('Ola sou uma pessoa e sei falar')

x = Animal('Branco','Feminino',4)
x.falar()
x.andar()
x.amamentar()