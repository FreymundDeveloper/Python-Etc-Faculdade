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


class Camisa(Roupa):
    _tipo = None
    _botoes = None
    _bolsos = None
    _gola = None

    def __init__(self):
        super().__init__()
        self._tipo = 'Nenhuma'
        self._botoes = '0'
        self._bolsos = '0'
        self._gola = True

    def ler_dados(self):
        self._tipo = input('Tipo: ')
        self._botoes = input('Botoes: ')
        self._bolsos = input('Bolsos: ')
        self._gola = input('Gola(s/n): ')
        if str.lower(self._gola) == 's':
            self._gola = True
        else:
            self._gola = False
        Roupa.ler_dados(self)

    def dados(self):
        print('Tipo: %s\n'
              'Botoes: %s\n'
              'Bolsos: %s\n'
              'Gola %s\n'
              % (self._tipo, self._botoes, self._bolsos, self._gola))
        Roupa.dados(self)


#############################################

v = []
x = 0
z = 0
c = False

while x is not 5:
    x = int(input('1)Objetos camisa:\n'
                  '2)Leitura de dados:\n'
                  '3)Calcular\n'
                  '4)Imprimir dados:\n'
                  '5)Sair: '))

    if x is 1:
        z = int(input('Quantas peças serão registradas: '))
        y = 0
        while y < z:
            peca = Camisa()
            v.append(peca)
            y += 1
        c = True

    elif x is 2 and c is True:
        y = 0
        while y < z:
            v[y].ler_dados()
            y += 1

    elif x is 3 and c is True:
        for e in v:
            print(e.calular())

    elif x is 4 and c is True:
        for e in v:
            e.dados()

    else:
        print('OPÇ INVALIDA')
