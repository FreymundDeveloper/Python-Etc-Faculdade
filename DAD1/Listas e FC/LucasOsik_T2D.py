class No:
    def __init__(self):
        self.__int = None
        self.__prox = None

    def getInt(self):
        return self.__int

    def setInt(self, intr):
        self.__int = intr

    def getProx(self):
        return self.__prox

    def setProx(self, prox):
        self.__prox = prox


class List:

    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self, valor):
        temp = No()
        if temp:
            temp.setInt(valor)
            if self.__fim:
                self.__fim.setProx(temp)
                self.__fim = temp
            else:
                self.__ini = self.__fim = temp

    def ordn(self):
        self.push(int(input('Digite um valor: ')))
        if not self.__ini:
            print('Lista vazia.')
            return
        cofre = []
        temp_no = self.__ini

        while temp_no:
            cofre.append(temp_no.getInt())
            temp_no = temp_no.getProx()
        self.popall()

        count = 0
        lista = sorted(cofre)
        lista.reverse()
        while count < len(lista):
            self.push(lista[count])
            count += 1

    def printall(self):
        if not self.__ini:
            print('Lista vazia.')
            return
        saida = '\nLista: '
        temp_no = self.__ini

        while temp_no:
            saida += '  ' + str(temp_no.getInt())
            temp_no = temp_no.getProx()
        print(saida)

    def pop(self):
        if not self.__fim:
            print('Lista vazia.')
            return
        self.printall()
        valor = int(input('Qual elemento deseja excluir: '))
        temp = self.__ini
        if temp.getInt() is valor:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            return
        while temp.getProx():
            if temp.getProx().getInt() is valor:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()

    def popall(self):
        if self.__ini is None:
            print('Lista vazia.')
            return
        self.__ini = self.__fim = None
        print('Lista esvaziada')


####################################################################################################
l = List()

while True:
    op = int(input('1)Inserir elemento\n2)Excluir um elemento\n3)Consultar lista\n4)Esvaziar lista\n5)Sair: '))

    if op is 1:
        l.ordn()
    elif op is 2:
        l.pop()
    elif op is 3:
        l.printall()
    elif op is 4:
        l.popall()
    elif op is 5:
        break
    else:
        print('Opc Invalida')