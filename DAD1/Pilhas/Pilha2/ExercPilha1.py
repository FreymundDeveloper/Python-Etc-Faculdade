class No_pilha:
    _valor = None
    _proximo = None

    def __init__(self):
        self._valor = 0
        self._proximo = None

    def getValor(self):
        return self._valor

    def setValor(self, valor):
        self._valor = valor

    def getProximo(self):
        return self._proximo

    def setProximo(self, prox):
        self._proximo = prox


class Pilha:
    def __init__(self):
        self._topo = None

    def push(self):
        temp_no = No_pilha()

        if temp_no:
            temp_no.setValor(int(input("Entre com um valor: ")))
            temp_no.setProximo(self._topo)  #
            self._topo = temp_no  #

    def pop(self):
        if self._topo:
            print("\nValor a remover: ", self._topo.getValor())
            self._topo = self._topo.getProximo()  #

        else:
            print("Pilha vazia")

    def printall(self):

        if not self._topo:
            print("Pilha vazia")
            return
        temp_no = self._topo
        saida = "Pilha:\n"

        while temp_no:
            saida += str(temp_no.getValor()) + "\n"
            temp_no = temp_no.getProximo()
        print(saida)

    def last(self):  # A
        if self._topo:
            print(self._topo.getValor())

        else:
            print('Pilha vazia')

    def soma(self):

        if not self._topo:
            print('Pilha vazia')

        soma = 0
        tem_po = self._topo

        while tem_po:
            soma += tem_po.getValor()
            tem_po = tem_po.getProximo()
        print(soma)

    def med(self):

        if not self._topo:
            print('Pilha vazia')

        soma = 0
        cont = 0
        tem_po = self._topo

        while tem_po:
            soma += tem_po.getValor()
            tem_po = tem_po.getProximo()
            cont += 1
        print(soma / cont)


p = Pilha()

while True:
    op = int(input("\n1 - Empilhar\n2 – Desempilhar\n3 - Imprime apilha\n4 - Ultimo valor\n5 - soma\n6 - Media\n7 - "
                   "Sair:\n "))
    if op is 1:
        p.push()
    elif op is 2:
        p.pop()
    elif op is 3:
        p.printall()
    elif op is 4:
        p.last()
    elif op is 5:
        p.soma()
    elif op is 6:
        p.med()
    else:
        break
