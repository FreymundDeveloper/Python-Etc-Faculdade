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

    def push(self, valor):
        novo = No_lista()
        if novo:
            novo.setV(valor)
            if self.__fim:
                self.__fim.setP(novo)
                novo.setA(self.__fim)
                self.__fim = novo
            else:
                self.__inic = self.__fim = novo

    def ordn(self):
        self.push(int(input('\nDigite o valor a ser inserido na lista: ')))
        if not self.__inic:
            print('Lista vazia.')
            return
        cofre = []
        temp_no = self.__inic

        while temp_no:
            cofre.append(temp_no.getV())
            temp_no = temp_no.getP()
        self.pop_all()

        count = 0
        lista = sorted(cofre)
        while count < len(lista):
            self.push(lista[count])
            count += 1

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
            saida = 'Lista: \n'
            temp = self.__inic
            while temp:
                saida += (str(temp.getV()) + '\t')
                temp = temp.getP()
            print(saida)
        else:
            print('Lista vazia.')

    def pop_all(self):
        if not self.__inic or not self.__fim:
            print('Lista vazia.')
            return
        self.__inic = self.__fim = None


l = Lista()

while True:
    op = int(input('\n1)Inserir na lista'
                   '\n2)Excluir um elemento'
                   '\n3)Consultar a lista'
                   '\n4)Esvaziar a lista'
                   '\n5)Sair: '))

    if op is 1:
        l.ordn()
    elif op is 2:
        l.pop()
    elif op is 3:
        l.print_all()
    elif op is 4:
        l.pop_all()
        print('Lista esvaziada')
    elif op is 5:
        exit()
    else:
        print('Opcao invalida.')
