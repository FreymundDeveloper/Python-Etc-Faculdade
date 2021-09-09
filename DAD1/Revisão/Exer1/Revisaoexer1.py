class Imovel:
    _preco = None
    _enderco = None

    def __init__(self, preco, endereco):
        self._preco = preco
        self._enderco = endereco

    def __del__(self, preco, endereco):
        self._preco = preco
        self._enderco = endereco

    def spreco(self, preco):
        self._preco = preco

    def sendeco(self, endereco):
        self._enderco = endereco


class ImovelN(Imovel):
    _valorad = None

    def __init__(self,preco, endereco, valorad):
        super().__init__(preco,endereco)
        self._valorad = valorad

    def svalorad(self, valorad):
        self._valorad = valorad

    def gvalorad(self):
        return self._preco + self._valorad


class ImovelV(Imovel):
    _valord = None

    def __init__(self, preco, endereco, valord):
        super().__init__(preco, endereco)
        self._valord = valord

    def svalord(self, valord):
        self._valord = valord

    def gvalord(self):
        return self._preco - self._valord
