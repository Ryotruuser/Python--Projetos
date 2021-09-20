from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
computador = randint(0, 10)
cont = jogador = total = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()
    total = computador + jogador
    if escolha == 'I':
        if total % 2 == 1:
            cont += 1
            print('-'*15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU IMPAR')
            print('-' * 15)
            print('Você VENCEU!')
            print('=-' * 7)
            print('Vamos jogar novamente...')
            print('=-' * 7)
        if total % 2 == 0:
            print('-' * 15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
            print('-' * 15)
            print('Você PERDEU!')
            print('=-' * 7)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
    if escolha == 'P':
        if total % 2 == 0:
            cont += 1
            print('-'*15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
            print('-' * 15)
            print('Você VENCEU!')
            print('=-' * 7)
            print('Vamos jogar novamente...')
            print('=-' * 7)
        if total % 2 == 1:
            print('-' * 15)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU IMPAR')
            print('-' * 15)
            print('Você PERDEU!')
            print('=-' * 7)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
