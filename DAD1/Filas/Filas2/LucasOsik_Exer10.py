class Fila_no:
    def __init__(self):
        self.__valor = 0
        self.__prox = None

    def setV(self, v):
        self.__valor = v

    def setP(self, p):
        self.__prox = p

    def getV(self):
        return self.__valor

    def getP(self):
        return self.__prox


class Fila:
    def __init__(self):
        self.__inic = None
        self.__fim = None

    def push(self, valor):
        new = Fila_no()
        if new:
            new.setV(valor)
            if self.__fim:
                self.__fim.setP(new)
                self.__fim = new
            else:
                self.__inic = self.__fim = new

    def pop(self):
        if self.__fim:
            saida = []
            temp = self.__inic
            while temp:
                saida.append(str(temp.getV()))
                temp = temp.getP()

            saida.reverse()
            print('*'.join(saida))

        if self.__fim:
            temp = self.__inic
            while temp:
                if self.__inic:
                    self.__inic = self.__inic.getP()
                    temp = self.__inic
                    if not self.__inic:
                        self.__fim = None
                        self.__inic = None

            print('Fila esvaziada')

        else:
            print("Fila vazia.")


#############################################################################################################

f = Fila()

while True:
    op = int(input('\n1)Entrada\n2)Imprime e esvazia\n3)Sair\nOPC:'))

    if op is 1:
        base = 2
        valor = (int(input('Digite um valor inteiro >1: ')))
        while valor != 1:
            if valor % base == 0:
                f.push(base)
                valor = valor / base
            else:
                base += 1

    elif op is 2:
        f.pop()

    elif op is 3:
        break

    else:
        print('OPC invalida')