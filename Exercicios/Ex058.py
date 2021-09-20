from random import randint
n = 0
p = 0
c = randint(0, 10)
ran = 0
print('Sou seu computador...')
print('Acabei de pensar em um número ente 0 e 10')
print('Será que você consegue advinhar qual foi ?')
while ran != c:
    ran = int(input('Seu palpite: '))
    p += 1
    if ran < c:
        print('Mais... tente novamente')
    if ran > c:
        print('Menos... tente novamente')
    if ran == c:
        print('Acertou com {} tentativas'.format(p))