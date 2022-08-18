class Itens:  # 1
    _qiv = None
    _ncivm = None
    _pi = None
    _vt = None

    def __init__(self):
        self._qiv = 0
        self._ncivm = []
        self._pi = []
        self._vt = 0

    def pedido(self):
        c = True
        while c is True:
            self._ncivm.append(input('Qual item deseja pedir:'))
            a = float(input('Qual o valor do item:'))
            self._vt += a
            self._pi.append(a)
            self._qiv += 1

            op = input('Deseja mais alguma coisa(S/N):')
            if op is 'N':
                c = False

    def valor(self):
        print('R$',self._vt)

    def dados(self):
        i = 0
        while i < len(self._ncivm):
            print('Item:', self._ncivm[i], ' Valor: R$', self._pi[i])
            i += 1

        print('\nValor total:', self._vt, '\nNumero de pedidos:', self._qiv)


class Mesa(Itens):
    _nome = None
    _num = None

    def __init__(self):
        super().__init__()
        self._nome = None
        self._num = None

    def pedido(self):
        self._nome = input('Digite seu nome: ')
        self._num = int(input('Digite o numero da mesa: '))
        super().pedido()

    def dados(self):
        print('\nNome do cliente:', self._nome, '\nNumero da mesa:', self._num)
        super().dados()


##################################################################################################################
p = Mesa()

while True:
    op = int(input('1)Leitura de dados\n2)Calcular despezas\n3)Imprime dados:'))

    if op is 1:
        p.pedido()
    elif op is 2:
        p.valor()
    elif op is 3:
        p.dados()
    else:
        break
