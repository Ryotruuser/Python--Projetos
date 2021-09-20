valor = int(input('Preço das compras R$ '))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção? '))
avista = valor - valor * (10 / 100)  # Desconto de 10% a vista dinheiro/cheque
avtcar = valor - valor * (5 / 100)  # Desconto de 5% a vista no carão
cartao = valor + valor * (20 / 100)  # Juros de 20% Cartão
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, avista))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, avtcar))
elif opcao == 3:
    print('Sua compra vai custar R${:.2f} no final.'.format(valor))
elif opcao == 4:
    par = int(input('Quantas parcelas? '))  # Numero de parcelas
    pavar = cartao / par  # Preço parcelado
    print('Sua compra será parcelada em {}X de R${} COM JUROS'.format(par, pavar))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, cartao))
else:
    print('Operação Invalida, tente novamente.')
