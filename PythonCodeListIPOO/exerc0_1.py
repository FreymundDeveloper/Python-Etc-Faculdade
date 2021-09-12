class Conta:
    numero = None
    titular = None
    saldo = None

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        self.saldo -= valor

    def deposite(self, valor):
        self.saldo += valor

    def vsdc(self):
        return self.saldo


c1=Conta(1234, str('Marcus Pontes'), 1000.00)
c2=Conta(4433, str('Ana Paula'), 1200.00)
c2.deposite(150)
c1.deposite(230)
c1.sacar(85)
print(c1.vsdc())
print(c2.vsdc())
