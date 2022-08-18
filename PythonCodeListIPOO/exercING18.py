class Ingresso:
    _valor = None

    def __init__(self, valor):
        self._valor = valor

    def Impv(self):
        return self._valor


class IVip(Ingresso):
    _valorAdic = None

    def __init__(self, valor):
        super().__init__(valor)
        self._valorAdic = self._valor * 0.25

    def Rvi(self):
        return self._valor + self._valorAdic


class In(Ingresso):

    def __init__(self, valor):
        super().__init__(valor)

    def Iin(self):
        return 'Ingresso normal'


class CI(IVip):
    _local = None

    def __init__(self, valor, local):
        super().__init__(valor)
        self._local = local

    def Al(self, local):
        self._local = local

    def Rl(self):
        return self._local


class CS(IVip):
    _valorAdic2 = None

    def __init__(self, valor, ):
        super().__init__(valor, )
        self._valorAdic2 = self._valor * 0.40

    def Rvi(self):
        return self._valor + self._valorAdic2


x = Ingresso(20)
print('R$', x.Impv())
x = IVip(20)
print('VIP R$', x.Rvi())
x = In(20)
print(x.Iin())
x = CI(20, 'Qualquer coisa')
print('Local:', x.Rl())
x = CS(20)
print('Camarote Superior R$', x.Rvi())
