def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

for c in range(1, 11):
    print(f'O fatorial de {c} e {fatorial(c)}')