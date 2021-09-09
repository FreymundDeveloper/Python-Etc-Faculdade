class Bank:
    __usuario = None
    __conta = None
    __tel = None

    def __init__(self, usuario, conta, tel):
        self.__usuario = usuario
        self.__conta = conta
        self.__tel = tel

    def rusuario(self, usuario):
        self.__usuario = usuario

    def rconta(self, conta):
        self.__conta = conta

    def rtel(self, tel):
        self.__tel = tel

    def sacar(self, valor):
        if self.__conta < valor:
            print('ERRO... valor da conta insuficiente')
        else:
            self.__conta -= valor

    def depositar(self, valor):
        self.__conta += valor

    def dados(self):
        return str('Usuario: %s \nTelefone: %s \nSaldo %2.f' % (self.__usuario, self.__tel, self.__conta))


c = Bank(None, None, None)
x = 0
while x != 2:
    x = int(input('1)Criar usuario; \n2)Sair;'))
    if x is 1:
        c.rusuario(input('Digite o seu nome:'))
        c.rconta(float(input('Digite o valor do seu saldo:')))
        c.rtel(input('Digite o seu telefone:'))
        z = 0
        while z != 4:
            z = int(input('1)Para sacar;\n2)Para depositar;\n3)Exibir dados;\n4)Sair;'))
            if z is 1:
                c.sacar(float(input('Digitar valor a sacar:')))
            if z is 2:
                c.depositar(float(input('Digite o valor a depositar')))
            if z is 3:
                print(c.dados())
