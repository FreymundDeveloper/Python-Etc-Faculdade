class No_lista:
    def __init__(self):
        self.__ant = None
        self.__valor = 0
        self.__prox = None

    def setA(self, a):
        self.__ant = a

    def setV(self, v):
        self.__valor = v

    def setP(self, p):
        self.__prox = p

    def getA(self):
        return self.__ant

    def getV(self):
        return self.__valor

    def getP(self):
        return self.__prox


class Lista:
    def __init__(self):
        self.__inic = None
        self.__fim = None

    def push_end(self, valor):
        novo = No_lista()
        if novo:
            novo.setV(valor)
            if self.__fim:
                self.__fim.setP(novo)
                novo.setA(self.__fim)
                self.__fim = novo
            else:
                self.__inic = self.__fim = novo

    def push_first(self, valor):
        novo = No_lista()
        if novo:
            novo.setV(valor)
            if self.__fim:
                novo.setP(self.__inic)
                self.__inic.setA(novo)
                self.__inic = novo
            else:
                self.__inic = self.__fim = novo

    def pop(self):
        if not self.__inic:
            print('Lista vazia')
            return
        self.print_all()
        valor = int(input('Qual elemento acima deseja excluir: '))
        if self.__inic.getV() == valor:
            self.__inic = self.__inic.getP()
            if not self.__inic:
                self.__fim = None
            else:
                self.__inic.setA(None)
        elif self.__fim.getV() == valor:
            self.__fim = self.__fim.getA()
            if not self.__fim:
                self.__inic = None
            else:
                self.__fim.setP(None)
        else:
            temp = self.__inic
            while temp.getP():
                if temp.getV() == valor:
                    temp.getP().setA(temp.getA())
                    temp.getA().setP(temp.getP())
                    break
                else:
                    temp = temp.getP()

    def print_all(self):
        if self.__fim:
            saida = "Lista: \n"
            temp = self.__inic
            while temp:
                saida += (str(temp.getV()) + "\t")
                temp = temp.getP()
            print(saida)
        else:
            print("Lista vazia.")

    def pop_all(self):
        if not self.__inic or not self.__fim:
            print('Lista vazia.')
            return
        self.__inic = self.__fim = None
        print('Lista esvaziada')


l = Lista()

while True:
    op = int(input("\n1)Inserir no final da lista"
                   "\n2)Inserir no início da lista"
                   "\n3)Excluir um elemento"
                   "\n4)Consultar a lista"
                   "\n5)Esvaziar a lista"
                   "\n6)Sair: "))

    if op is 1:
        valor = int(input("\nDigite o valor a ser inserido no final: "))
        l.push_end(valor)
    elif op is 2:
        valor = int(input("\nDigite o valor a ser inserido no inicio: "))
        l.push_first(valor)
    elif op is 3:
        l.pop()
    elif op is 4:
        l.print_all()
    elif op is 5:
        l.pop_all()
    elif op is 6:
        exit()
    else:
        print("Opcao invalida.")
