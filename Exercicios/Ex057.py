n = 0
m = 0
f = 0
while n != 1:
    n = str(input('Informe seu genero: ')).upper()
    if n == 'M':
        m += 1
        print('Sexo M registrado com sucesso')
        n = m
    elif n == 'F':
        f += 1
        print('Sexo F registrado com sucesso')
        n = f
    elif n != 'M' and n != 'F':
        while n != 1:
            n = str(input('Dados invalidos. Por favor digite seu genero correto: ')).upper()
            if n == 'M':
                m += 1
                print('Sexo M registrado com sucesso')
                n = m
            elif n == 'F':
                f += 1
                print('Sexo F registrado com sucesso')
                n = f