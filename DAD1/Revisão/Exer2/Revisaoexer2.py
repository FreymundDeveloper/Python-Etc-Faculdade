class Calculadora:
    _valorA = None
    _valorB = None

    def __init__(self, valorA, valorB):
        self._valorA = valorA
        self._valorB = valorB

    def __del__(self, valorA, valorB):
        self._valorA = valorA
        self._valorB = valorB

    def lervalorA(self, valorA):
        self._valorA = valorA

    def lervalorB(self, valorB):
        self._valorB = valorB

    def soma(self):
        return self._valorA + self._valorB

    def subtrasao(self):
        return self._valorA - self._valorB

    def multiplicar(self):
        return self._valorA * self._valorB

    def divisao(self):
        return self._valorA / self._valorB

