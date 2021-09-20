class Conta:
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo

    def __str__(self): # retorna uma str com informações
        return f'ID: {self.ID} \nSaldo: R$ {self.saldo}'

    def __add__(self, other): # incrementar um valor
        self.saldo += other.saldo

Bradesco = Conta(456, 2000)
print(Bradesco)

Itau = Conta(555, 10000)
Itau + Bradesco
print(Bradesco.saldo)
