class Imovel:

    _endereco = None
    _preco = None

    def __init__(self, endereco, preco):
        self._endereco =endereco
        self._preco = preco


class IN(Imovel):

    _valora = None

    def __init__(self, endereco, preco, valora):
        super().__init__(endereco, preco)
        self._valora = valora

    def acva(self, valora):
        self._valora = valora

    def rva(self):
        return self._valora


class IV(Imovel):

    _valord = None

    def __init__(self, endereco, preco, valord):
        super().__init__(endereco, preco)
        self._valord = valord

    def acvd(self, valord):
        self._valord = valord

    def rvd(self):
        return self._valord


i = IN('Rio', 20000, 5000)
print('IMOVEL NOVO \nEndereço: %s \nPreço R$ %2.f \nValor adicional R$ %2.f \nValor total R$ %2.f \n' % (i._endereco, i._preco, i.rva(), i._preco + i.rva()))
i = IV('SP', 20000, 5000)
print('IMOVEL VELHO \nEndereço: %s \nPreço R$ %2.f \nValor desconto R$ %2.f \nValor total R$ %2.f\n' % (i._endereco, i._preco, i.rvd(), i._preco - i.rvd()))