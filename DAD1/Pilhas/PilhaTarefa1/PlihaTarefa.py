class Pilha_No:
    _valor = None
    _prox = None

    def __init__(self):
        self._valor = 0
        self._prox = None

    def setV(self, v):
        self._valor = v

    def getV(self):
        return self._valor

    def setP(self, p):
        self._prox = p

    def getP(self):
        return self._prox


class Pilha:
    def __init__(self):
        self._topo = None
        self._p1 = [34, 2, 1, 2]
        self._p2 = [22, 14, 5]

    def push(self, a):
        temp = Pilha_No()

        if temp:
            temp.setV(a)
            temp.setP(self._topo)
            self._topo = temp

    def pop(self):
        if self._topo:
            self._topo = self._topo.getP()
        else:
            print('Pilha vazia')

    def juntar(self):
        junt = self._p1 + self._p2
        junt2 = []
        x = len(junt) - 1
        maiorvalor = junt[x]
        menorvalor = junt[x]
        result = None
        c = True
        verf = None

        while x >= 0:
            y = len(junt) - 1

            while y >= 0:
                if c:
                    if junt[y] > maiorvalor:
                        maiorvalor = junt[y]

                    if junt[y] < menorvalor:
                        menorvalor = junt[y]

                elif maiorvalor > junt[y] >= verf:
                    result = junt[y]
                    verf = junt[y]

                y -= 1

            if not c:
                maiorvalor = result

            y = -1
            for i in junt:
                if i == maiorvalor:
                    y += 1

            if y > 0:
                x -= y

            while y >= 0:
                junt2.append(maiorvalor)
                y -= 1

            verf = menorvalor
            c = False
            x -= 1

        x = len(junt2) - 1

        while x >= 0:
            self.push(junt2[x])
            x -= 1

    def printall(self):

        if not self._topo:
            print("Pilha vazia")
            return
        temp_no = self._topo
        saida = "Pilha:\n"

        while temp_no:
            saida += str(temp_no.getV()) + "\n"
            temp_no = temp_no.getP()
        print(saida)


p = Pilha()

p.juntar()
p.printall()
