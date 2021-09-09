class Node:
    def __init__(self):
        self.__n = 0
        self.__x = 0
        self.__y = 0
        self.__prox = None

    def setN(self, n):
        self.__n = n

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setProximo(self, p):
        self.__prox = p

    def getN(self):
        return self.__n

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getProximo(self):
        return self.__prox


class Pilha:
    def __init__(self):
        self.__topo = None

    def getTopo(self):
        return self.__topo

    def setTopo(self, topo):
        self.__topo = topo

    def push(self, n):
        temp_no = Node()
        if temp_no:
            if n > 0:
                temp_no.setN(n)
                temp_no.setX(n - 1)
                temp_no.setProximo(self.__topo)
                self.__topo = temp_no
                self.push(n - 1)
            else:
                temp_no.setProximo(self.__topo)
                self.__topo = temp_no

    def pop(self):
        temp_no = Node()
        if self.__topo:
            temp_no = self.__topo
            self.setTopo(self.__topo.getProximo())
            if self.__topo:
                if self.__topo.getX() is not 0:
                    self.__topo.setY(self.__topo.getX() + temp_no.getY())
                else:
                    self.__topo.setY(0)
                self.pop()
            else:
                if temp_no.getN() + temp_no.getY() is not 0:
                    print("Soma:", temp_no.getN() + temp_no.getY())
                else:
                    print("Soma: 1")
        else:
            print("Pilha vazia...")


p = Pilha()
numero = int(input('Calcular a Soma sucessiva de: '))
p.push(numero)
p.pop()
