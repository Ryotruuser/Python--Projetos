def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show:(opcional) mostrar ou não a conta
    :return:O valor do fatorial de um numero n.
    """
    from math import factorial
    if show == True:
        for c in range(n, 0, -1):
            print(f'{c}', end=' ')
            if c > 1:
                print('X', end=' ')
        print('=', end=' ')
        return factorial(n)
    else:
        return factorial(n)


print(fatorial(5, show=True))
help(fatorial)