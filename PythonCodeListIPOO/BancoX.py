class Bank:
    _usuario = None
    _conta = None
    _tel = None
    _operacoes = None

    def __init__(self, usuario, conta, tel):
        self._usuario = usuario
        self._conta = conta
        self._tel = tel
        self._operacoes = []

    def rusuario(self, usuario):
        self._usuario = usuario

    def rconta(self, conta):
        self._conta = conta

    def rtel(self, tel):
        self._tel = tel

    def sacar(self, valor):
        if self.ver(valor) is True:
            print('ERRO... valor da conta insuficiente')
        else:
            self._conta -= valor
            self._operacoes.append(['Sacar:', valor])

    def ver(self, valor):
        if self._conta < valor:
            return True
        else:
            return False

    def depositar(self, valor):
        self._conta += valor
        self._operacoes.append(['Depositar:', valor])

    def dados(self):
        return str('Usuario: %s \nTelefone: %s \nSaldo %2.f' % (self._usuario, self._tel, self._conta))

    def extr(self):
        for x in self._operacoes:
            print(x[0])


class BankEsp(Bank):
    __limite = None

    def __init__(self, usuario, conta, tel, limite):
        super().__init__(usuario, conta, tel)
        self.__limite = limite

    def ver(self, valor):
        if self._conta + self.__limite <= valor:
            return True
        else:
            return False

    def depositar(self, valor):
        self._conta += valor
        self._operacoes.append(['Depositar: %2.f \nExtrato disponivel: %2.f' % (valor, self._conta + self.__limite)])
