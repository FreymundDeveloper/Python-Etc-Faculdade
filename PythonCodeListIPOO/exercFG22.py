class FG:
    _area = None
    _peri = None

    def __init__(self, area, peri):
        self._area = area
        self._peri = peri

    def __del__(self):
        self._area = None
        self._peri = None

    def ra(self):
        return self._area

    def rp(self):
        return self._peri


class Retangulo(FG):

    def __init__(self, area, peri):
        super().__init__(area, peri)

    def ca(self):
        alt = float(input('Informe a altura:'))
        base= float(input('Informe a base:'))
        return alt * base

    def cp(self):
        alt = float(input('Informe a altura:'))
        base = float(input('Informe a base:'))
        return (alt + base)* 2


class Quadrado(Retangulo):

    def __init__(self, area, peri):
        super().__init__(area, peri)

    def ca(self):
        lados = float(input('Informe o valor dos lados'))
        return lados ** 2

    def cp(self):
        lados = float(input('Informe o valor dos lados'))
        return lados * 4


class Triangulo(FG):

    def __init__(self, area, peri):
        super().__init__(area, peri)

    def ca(self):
        alt = float(input('Informe a altura:'))
        base = float(input('Informe a base:'))
        return (alt * base)/ 2

    def cp(self):
        l1= float(input('Informe o valor do lodo:'))
        l2 = float(input('Informe o valor do lodo:'))
        l3 = float(input('Informe o valor do lodo:'))
        return l1 + l2 + l3


class Circulo(FG):

    def __init__(self, area, peri):
        super().__init__(area, peri)

    def ca(self):
        r = float(input('Informe o raio:'))
        return 4 * 3.14 * (r ** 2)

    def cp(self):
        r = float(input('Informe o raio:'))
        return 2 * 3.14 * r


