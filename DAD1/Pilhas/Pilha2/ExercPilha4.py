class No_pilha:
    _tudo = None
    _proximo = None
    _menino = None
    _pmenino = None
    _menina = None
    _pmenina = None

    def __init__(self):
        self._tudo = None
        self._proximo = None
        self._menino = None
        self._pmenino = None
        self._menina = None
        self._pmenina = None

    def getTudo(self):
        return self._tudo

    def setTudo(self, tudo):
        self._tudo = tudo

    def getProximo(self):
        return self._proximo

    def setProximo(self, prox):
        self._proximo = prox

    def getMenino(self):
        return self._menino

    def setMenino(self, mo):
        self._menino = mo

    def getPmenino(self):
        return self._pmenino

    def setPmenino(self, pmo):
        self._pmenino = pmo

    def getMenina(self):
        return self._menina

    def setMenina(self, ma):
        self._menina = ma

    def getPmenina(self):
        return self._pmenina

    def setPmenina(self, pma):
        self._pmenina = pma


class Pilha:
    def __init__(self):
        self._tmo = None
        self._tma = None
        self._topo = None
        self._mmo = 0
        self._mma = 0
        self._cmo = 0
        self._cma = 0
        self._verif = False

    def mopush(self):
        temp_no = No_pilha()

        if temp_no:
            temp_no.setMenino(int(input("Entre com um valor: ")))
            self._mmo += temp_no.getMenino()
            temp_no.setPmenino(self._tmo)  #
            self._tmo = temp_no  #
            temp_no.setTudo(temp_no.getMenino())
            temp_no.setProximo(self._topo)
            self._topo = temp_no
            self._cmo += 1
            self._verif = True

    def mapush(self):
        temp_no = No_pilha()

        if temp_no:
            temp_no.setMenina(int(input("Entre com um valor: ")))
            self._mma += temp_no.getMenina()
            temp_no.setPmenina(self._tma)  #
            self._tma = temp_no  #
            temp_no.setTudo(temp_no.getMenina())
            temp_no.setProximo(self._topo)
            self._topo = temp_no
            self._cma += 1
            self._verif = True

    def juntar(self):
        if not self._topo:
            print('Pilha vazia')
            return
        temp_no = self._topo
        saida = 'notas:\n'

        while temp_no:
            saida += str(temp_no.getTudo()) + '\n'
            temp_no = temp_no.getProximo()
        print(saida)

    def med(self):
        if self._verif is True:
            if self._cmo > 0:
                print('Media menino:', self._mmo / self._cmo)

            else:
                print('Pilha vazia')

            if self._cma > 0:
                print('Media menino:', self._mma / self._cma)

            else:
                print('Pilha vazia')

            if self._cmo == 0 and self._cma == 0:
                print('Pilha vazia')

            else:
                print('Media Total:', (self._mmo + self._mma) / (self._cmo + self._cma))

        else:
            print('Pilha vazia')


#####################################################################################################################
p = Pilha()

while True:
    op = int(
        input('\n1)Entrar nota de Menino\n2)Entrar nota de menina\n3)Retornar lista compleata\n4)Media das listas:'))

    if op is 1:
        p.mopush()
    elif op is 2:
        p.mapush()
    elif op is 3:
        p.juntar()
    elif op is 4:
        p.med()
    else:
        break
