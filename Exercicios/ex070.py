print('-=' * 15)
print('       Lojas Americanas')
print('-=' * 15)
total = masm = menor = cont = 0
barato = ''
while True:
        nome = str(input('Nome do produto: '))
        produto = float(input('Preço do produto R$'))
        cont += 1
        total += produto
        if produto > 1000:
            masm += 1
        if cont == 1 or produto < menor:
            menor = produto
            barato = nome
        fim = str(input('Quer continuar [S/N] ')).upper().strip()[0]
        while fim not in 'SN':
            fim = str(input('Quer continuar [S/N] ')).upper().strip()[0]
        if fim == 'N':
            break
print('=-'*20)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {masm} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
