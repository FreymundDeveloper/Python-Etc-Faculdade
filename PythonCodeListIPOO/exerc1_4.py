class Bola:
    cor = None
    circ = None
    mat = None

    def __init__(self, cor, circ, mat):
        self.cor = cor
        self.circ = circ
        self.mat = mat

    def tcor(self, cor):
        self.cor = cor

    def mcor(self, cor):
        return self.cor


c1 = Bola(None, None, None)
c1.tcor(input('Digite uma cor:'))
print(c1.mcor(str))
