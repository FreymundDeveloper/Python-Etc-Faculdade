class CDB:
    _ni = None
    _alt = None
    _ps = None

    def __init__(self):
        self._ni = None
        self._alt = None
        self._ps = None

    def __del__(self):
        self._ni = None
        self._alt = None
        self._ps = None

    def cadastro(self, a, b, c):
        self._ni = a
        self._alt = b
        self._ps = c

    def aval(self):
        x = 0
        while x < len(self._ni):
            if (self._ps[x] / self._alt[x] ** 2) < 18:
                print(self._ni[x])
            x += 1
