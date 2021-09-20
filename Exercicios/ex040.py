nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
if media < 4.9:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
print(media)
