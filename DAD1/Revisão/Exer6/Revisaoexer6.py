class UN:
    _mat = None
    _sexo = None
    _n1 = None
    _n2 = None

    def __init__(self):
        self._mat = None
        self._sexo = None
        self._n1 = None
        self._n2 = None

    def __del__(self):
        self._mat = None
        self._sexo = None
        self._n1 = None
        self._n2 = None

    def inf(self, a, b, c, d):
        self._mat = a
        self._sexo = b
        self._n1 = c
        self._n2 = d

    def ap(self):
        x = 0
        while x < len(self._mat):
            if ((self._n1[x] + self._n2[x]) / 2) >= 7:
                print(self._mat[x])
            x += 1

    def exa(self):
        x = 0
        while x < len(self._mat):
            if ((self._n1[x] + self._n2[x]) / 2) < 7:
                print(self._mat[x])
            x += 1

    def mm(self):
        x = 0
        ml = (self._n1[x] + self._n2[x]) / 2
        mn = (self._n1[x] + self._n2[x]) / 2
        mla = self._mat[x]
        mna = self._mat[x]
        while x < len(self._mat):
            if mn > (self._n1[x] + self._n2[x]) / 2:
                mn = (self._n1[x] + self._n2[x]) / 2
                mna = self._mat[x]

            if ml < (self._n1[x] + self._n2[x]) / 2:
                ml = (self._n1[x] + self._n2[x]) / 2
                mla = self._mat[x]

            x += 1
        print('Melhor aluno:', mla, '\n Media: %.2f' % ml)
        print('Pior aluno:', mna, '\n Media: %.2f ' % mn)
