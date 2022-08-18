class Contc:
    nn = None
    nc = None
    saldo = None

    def __init__(self, nn, nc, saldo):
        self.nn = nn
        self.nc = nc
        self.saldo = saldo

    def altn(self, nc):
        self.nc = nc

    def dep(self, valor):
        self.saldo += valor
        if self.saldo > 0:
            print(str('Valor do saldo:'), self.saldo)

    def sac(self, valor):
        self.saldo -= valor
        if self.saldo > 0:
            print(str('Valor do saldo:'), self.saldo)


c1 = Contc(None, None, None)
c1.nc = (float(input('Digite o numero da conta:')))
c1.nn = (input('Digite o seu nome:'))
c1.saldo = float(input('Qual o valor em sua conta:'))
x = 0
while x != 3:
    x = int(input('1)Deposito:\n2)Saque:\n3)Sair:'))
    if x is 1:
        c1.dep(float(input('Quanto quer Depositar:')))
    elif x is 2:
        c1.sac(float(input('Quanto quer sacar:')))
