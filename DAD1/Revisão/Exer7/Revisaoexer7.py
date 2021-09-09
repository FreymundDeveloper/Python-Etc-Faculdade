class CDC:
    _gab = None
    _mat = None
    _resp = None

    def __init__(self):
        self._gab = None
        self._mat = None
        self._resp = None

    def __del__(self):
        self._gab = None
        self._mat = None
        self._resp = None

    def gabt(self, a):
        self._gab = a

    def an(self, m, r):
        self._mat = m
        self._resp = r

        x = 0
        y = 2
        c = 0
        f = 0
        v = 0
        apr = 0
        ms = []

        while x < len(self._mat):
            z = 0
            acrt = 0
            while z < len(self._gab):
                if self._resp[v] is self._gab[z]:
                    acrt += 2
                z += 1
                v += 1
            ms.append(acrt)
            if acrt > 7:
                apr += 1
            print('Aluno %.i Tirou %.2f ' % (int(self._mat[x]), acrt))
            x += 1
        print('Media de aprovados:', (apr / len(self._mat)) * 100)
        while y <= 10:
            if ms.count(y) > c:
                c = ms.count(y)
                f = y
            y += 2
        print('A nota que mais apareceu é ', f)
