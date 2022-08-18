class Est:
    __nome = None
    __sigla = None
    __cidades = None

    def __init__(self, nome, sigla, cidades):
        self.__nome = nome
        self.__sigla = sigla
        self.__cidades = cidades

    def ene(self, nome):
        self.__nome = nome

    def rne(self):
        return self.__nome

    def ese(self, sigla):
        self.__sigla = sigla

    def rse(self):
        return self.__sigla

    def ece(self, cidades):
        self.__cidades = cidades

    def rce(self):
        return self.__cidades


class Cidade:
    __nc = None
    __pp = None

    def __init__(self, nc, pp):
        self.__nc = nc
        self.__pp = pp

    def enc(self, nc):
        self.__nc = nc

    def rnc(self):
        return self.__nc

    def epp(self, pp):
        self.__pp = pp

    def rpp(self):
        return self.__pp


est1 = Est('Jorgas', 'JG', None)
e1c1 = Cidade('Celulite', 10000)
e1c2 = Cidade('Org', 5000)
est1.ece(e1c1.rpp() + e1c2.rpp())
est2 = Est('Dement', 'DM', None)
e2c1 = Cidade('Pont', 15000)
e2c2 = Cidade('Jocasta', 50000)
est2.ece(e2c1.rpp() + e2c2.rpp())
est3 = Est('Duminigão', 'DN', None)
e3c1 = Cidade('Xando', 100000)
e3c2 = Cidade('Celga', 500)
est3.ece(e3c1.rpp() + e3c2.rpp())
print('Estado %s população %i =' % (est1.rne(), est1.rce()))
print('Estado %s população %i =' % (est2.rne(), est2.rce()))
print('Estado %s população %i =' % (est3.rne(), est3.rce()))
