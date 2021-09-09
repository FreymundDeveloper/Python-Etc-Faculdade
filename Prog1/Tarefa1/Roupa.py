class Roupa:
    _mr = None
    _cr = None
    _tr = None
    _qpr = None
    _pr = None
    _ctpr = None

    def __init__(self):
        self._mr = 'vdd'
        self._cr = 'azul'
        self._tr = 'gg'
        self._qpr = '1'
        self._pr = '10.0'
        self._ctpr = '10.0'

    def __del__(self):
        self._mr = None
        self._cr = None
        self._tr = None
        self._pr = None
        self._qpr = None
        self._ctpr = None

    def ler_dados(self):
        self._mr = input('Marca: ')
        self._cr = input('Cor: ')
        self._tr = input('Tamanho: ')
        self._qpr = input('Quantidade: ')
        self._pr = input('Preço ')
        x = float(self._pr)
        y = int(self._qpr)
        self._ctpr = str(x * y)

    def calular(self):
        return self._ctpr

    def dados(self):
        print('Marca: %s\n'
              'Cor: %s\n'
              'Tamanho: %s\n'
              'Quantidade: %s\n'
              'Preço: %s\n'
              'Valor total: %s'
              % (self._mr, self._cr, self._tr, self._qpr, self._pr, self._ctpr))