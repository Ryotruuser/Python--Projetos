print('-='*10)
print('   MRV IMOBILIARIA')
print('-='*10)
valor1 = int(input('Qual valor da casa: R$ '))
salario = int(input('Salário do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento ? '))
ano = anos * 12
emprestimo = (30/100) * salario
conta = valor1 / ano
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(valor1,anos,conta))
if emprestimo >= conta:
    print('Empréstimo APROVAOD!')
else:
    print('Empréstimo NEGADO!')
