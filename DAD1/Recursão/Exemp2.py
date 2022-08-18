class Node:
    def __init__(self):
        self.__n = 0
        self.__x = 0
        self.__y = 0
        self.__proximo = None

    def getN(self):
        return self.__n

    def setN(self, n):
        self.__n = n

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getProximo(self):
        return self.__proximo

    def setProximo(self, proximo):
        self.__proximo = proximo


class Pilha:
    def __init__(self):
        self.__topo = None

    def getTopo(self):
        return self.__topo

    def setTopo(self, topo):
        self.__topo = topo

    def push(self, num):
        temp_no = Node()
        if temp_no:
            if num > 0:
                temp_no.setN(num)
                temp_no.setX(num - 1)
                temp_no.setProximo(self.__topo)
                self.__topo = temp_no
                self.printall(1)
                self.push(num - 1)
            else:
                temp_no.setN(0)
                temp_no.setX(0)
                temp_no.setY(1)
                temp_no.setProximo(self.__topo)
                self.__topo = temp_no
                self.printall(1)

    def pop(self):
        temp_no = Node()
        if self.__topo:
            temp_no = self.__topo
            self.setTopo(self.__topo.getProximo())
            if self.__topo:
                if self.__topo.getX() is not 0:
                    self.__topo.setY(self.__topo.getX() * temp_no.getY())
                else:
                    self.__topo.setY(1)
                self.printall(2)
                self.pop()
            else:
                if temp_no.getN() * temp_no.getY() is not 0:
                    print("Fatorial:", temp_no.getN() * temp_no.getY())
                else:
                    print("Fatorial: 1")
                self.printall(2)
        else:
            print("Pilha vazia...")

    def printall(self, push_pop):
        if not self.__topo:
            print("Pilha vazia...")
            return
        temp_no = self.__topo
        saida = "Pilha: n x y\n"
        while temp_no:
            if push_pop is 1:
                saida += "Push "
            else:
                saida += "Pop "
            saida += str(temp_no.getN()) + " " + str(temp_no.getX()) + \
                " " + str(temp_no.getY()) + "\n"
            temp_no = temp_no.getProximo()
        print(saida)


p = Pilha()
numero = int(input('Calcular o fatorial de: '))
p.push(numero)
p.pop()
