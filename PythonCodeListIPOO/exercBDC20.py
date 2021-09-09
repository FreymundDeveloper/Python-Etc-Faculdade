class BDC:
    _tipodc = None
    _valorl = None
    _qc = None

    def __init__(self, tipodc, valorl, qc):
        self._tipodc = tipodc
        self._valorl = valorl
        self._qc = qc

    def __del__(self):
        self._tipodc = None
        self._valorl = None
        self._qc = None

    def apv(self):
        v = float(input('valor:'))
        if self._qc > (v/self._valorl):
            self._qc -= v/self._valorl
        return v / self._valorl

    def apl(self):
        v = float(input('Litros:'))
        if self._qc > v:
            self._qc -= v
        return v * self._valorl

    def av(self):
        self._valorl = float(input('Digite valor:'))
        return self._valorl

    def ac(self):
        self._tipodc = input('Digite combustivel:')
        return self._tipodc

    def aqc(self):
        self._qc = float(input('Digite quantidade combustivel:'))
        return self._qc


bomba = BDC('GAS', 10, 5000)
x = 0
while x != 6:
    x = int(input('1)A.P.V; \n2)A.P.L; \n3)A.V; \n4)A.C; \n5)A.Q.C; \n6)SAIR;\n'))
    if x is 1:
        print(bomba.apv())
    if x is 2:
        print(bomba.apl())
    if x is 3:
        print(bomba.av())
    if x is 4:
        print(bomba.ac())
    if x is 5:
        print(bomba.aqc())