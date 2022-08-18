class PNO:
    _valor = None
    _prox = None

    def __init__(self):
        self._valor = 0
        self._prox = None

    def setValor(self, v):
        self._valor = v

    def getValor(self):
        return self._valor

    def setProx(self, p):
        self._prox = p

    def getProx(self):
        return self._prox


class Pilha:
    _topo = None

    def __init__(self):
        self._topo = None

    def push(self, valor):
        temp = PNO()

        if temp:
            temp.setValor(valor)
            temp.setProx(self._topo)
            self._topo = temp

    def printall(self):
        if not self._topo:
            print('Pilha vazia')

        else:
            temp = self._topo
            tex = ''

            while temp:
                tex += str(temp.getValor())
                temp = temp.getProx()
            return tex

    def popall(self):
        while self._topo is not None:
            self._topo = self._topo.getProx()

        print('\nPilha esvaziada\n')

    def convDec(self):
        temp = self._topo
        x = 0
        result = 0
        while temp:
            result += int(temp.getValor()) * (2**x)
            temp = temp.getProx()
            x += 1
        return result


#################################################################################################################
p = Pilha()

while True:
    op = int(input('1)Converter decimal para binario\n2)Converter binario para decimal\n3)limpar Pilha\n4)Sair:'))

    if op is 1:
        valor = int(input('Digite um valor inteiro positivo:'))
        while valor != 0:
            rest = valor % 2
            valor = int(valor / 2)
            p.push(rest)
        print(p.printall())

    elif op is 2:
        valor = int(input('Digite um valor binario:'))
        for i in str(valor):
            p.push(int(i))
        result = p.convDec()
        print(result)

    elif op is 3:
        p.popall()

    else:
        break

