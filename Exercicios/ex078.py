lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para o posição {c}: ')))

print('=-' * 30)
print(f'Você digitou {lista}')
print(f'O maior numero encontrado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print(f'O menor numero encontrado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')