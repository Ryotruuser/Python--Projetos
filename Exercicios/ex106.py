

def txt(txt):
    """
    -> Atribui simbolos antes e depois da palavra com comprimento da mesma
    :param txt: palavra que deseja
    :return: simbolos acima e sob a palavra que medem seu comprimento
    """
    a = len(txt) + 2
    print('~' * a)
    print('{}'.format(txt))
    print('~' * a)


def ajuda(n):
    """
    -> Ajuda o usuario a esclarecer duvidas sobre determinada função
    :param n: função que deseja saber mas sobre.
    :return: informações da função deseja, todas as informações e variações da mesma.
    """
    while True:
        from time import sleep
        sleep(0.3)
        print('\033[1;30;42m')
        txt('  SISTEMA DE AJUDA PYHELP')
        print('\033[m')
        a = str(input(n))
        if a == 'fim' or a == 'Fim':
            print('\033[1;30;41m ')
            txt(' ATE LOGO!')
            print('\033[m')
            break
        else:
            print('\033[1;30;44m')
            sleep(0.3)
            txt(f'  Acessando o manual do comando {a}')
            sleep(0.1)
            print('\033[1;37;40m')

            help(a)
            print('\033[m')





a = ajuda('Função da Biblioteca: ')