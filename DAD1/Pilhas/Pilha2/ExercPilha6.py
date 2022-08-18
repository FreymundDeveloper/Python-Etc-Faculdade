class Pilha_no:
    _valor = None
    _prox = None

    def __init__(self):
        self._valor = None
        self._prox = None

    def setValor(self, v):
        self._valor = v

    def getValor(self):
        return self._valor

    def setProx(self, v):
        self._prox = v

    def getProx(self):
        return self._prox


class Pilha:
    def __init__(self):
        self._topo = None

    def push(self, a):
        temp_no = Pilha_no()

        if temp_no:
            temp_no.setValor(a)
            temp_no.setProx(self._topo)
            self._topo = temp_no

    def pop(self):
        if self._topo:
            print('Valor a remover:', self._topo.getValor())
            self._topo = self._topo.getProx()

        else:
            print('Pilha vazia')

    def prinall(self):
        if not self._topo:
            print('Pilha vazia')
            return
        temp_no = self._topo
        saida = '\n'

        while temp_no:
            saida += str(temp_no.getValor()) + '\n'
            temp_no = temp_no.getProx()
        print(saida)

    def esc(self):
        pilha_n = Pilha()
        pilha_p = Pilha()

        while True:
            op = int(input('1)Entrar valor\n2)Imprimir pilhas\n3)Sair:'))

            if op is 1:
                a = int(input('digite um valor: '))
                if a > 0:
                    pilha_p.push(a)

                elif a < 0:
                    pilha_n.push(a)

                elif a == 0:
                    pilha_p.pop()
                    pilha_n.pop()

            elif op is 2:
                print('Pilha Positiva:')
                pilha_p.prinall()
                print('Pilha Negativa:')
                pilha_n.prinall()

            else:
                break


#################################################################################################
p = Pilha()

p.esc()
