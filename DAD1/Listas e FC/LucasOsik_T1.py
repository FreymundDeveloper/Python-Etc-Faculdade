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

    def push_end(self):
        temp = No()
        if temp:
            temp.setInt(int(input('Digite um numero: ')))
            if self.__fim:
                self.__fim.setProx(temp)
                self.__fim = temp
            else:
                self.__ini = self.__fim = temp

    def push_start(self):
        temp = No()
        if temp:
            temp.setInt(int(input('Digite um numero: ')))
            temp.setProx(self.__ini)
            if not self.__ini:
                self.__fim = temp
            self.__ini = temp

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
    op = int(input('1)Inserir no final\n2)Inserir no início\n3)Excluir um elemento\n4)Consultar lista\n5)Esvaziar '
                   'lista\n6)Sair: '))

    if op is 1:
        l.push_end()
    elif op is 2:
        l.push_start()
    elif op is 3:
        l.pop()
    elif op is 4:
        l.printall()
    elif op is 5:
        l.popall()
    elif op is 6:
        break
    else:
        print('Opc Invalida')
