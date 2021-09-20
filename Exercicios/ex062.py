print('=' * 21)
print('Progressão Aritmetica')
print('='* 21)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont != total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('A progressão foi finalizada com {} termos mostrados'.format(total))
