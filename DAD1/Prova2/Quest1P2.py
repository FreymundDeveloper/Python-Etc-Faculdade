class No:
    def __init__(self):
        self.__usuario = None
        self.__prox = None

    def getUsr(self):
        return self.__usuario

    def setUsr(self, usr):
        self.__usuario = usr

    def getProx(self):
        return self.__prox

    def setProx(self, prox):
        self.__prox = prox


class List:

    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self):
        temp = No()
        if temp:
            temp.setUsr(input('Digite um usuario(Nome(ESPAÇO)Valor): '))
            if self.__fim:
                self.__fim.setProx(temp)
                self.__fim = temp
            else:
                self.__ini = self.__fim = temp

    def printall(self):
        if not self.__ini:
            print('Lista vazia.')
            return
        saida = '\nLista: '
        temp_no = self.__ini

        while temp_no:
            saida += '  ' + str(temp_no.getUsr())
            temp_no = temp_no.getProx()
        print(saida)

    def pop(self, nome):
        if not self.__fim:
            print('Lista vazia.')
            return
        usr = nome
        temp = self.__ini
        if temp.getUsr() is usr:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            return
        while temp.getProx():
            if temp.getProx().getUsr() is usr:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()

    def exf(self):
        if not self.__ini:
            print('Lista vazia.')
            return

        self.printall()
        escolha = input('Escolha o nome de quem vc quer excluir:')
        temp_no = self.__ini

        while temp_no:
            usuario = str(temp_no.getUsr())
            analise = usuario.split()
            nome = analise[0]
            if escolha == nome:
                self.pop(usuario)

            temp_no = temp_no.getProx()

    def sm(self):
        if not self.__ini:
            print('Lista vazia.')
            return

        temp_no = self.__ini
        salario = 0.0
        maior = []

        while temp_no:
            usuario = str(temp_no.getUsr())
            analise = usuario.split()
            comp = analise[1]
            if float(comp) >= salario:
                if float(comp) == salario:
                    maior.append(usuario)
                elif float(comp) > salario:
                    maior.clear()
                    maior.append(usuario)
                    salario = float(comp)
            temp_no = temp_no.getProx()
        print(maior)

    def med(self):
        if not self.__ini:
            print('Lista vazia.')
            return
        media = 0
        temp_no = self.__ini
        cont = 0

        while temp_no:
            usuario = str(temp_no.getUsr())
            analise = usuario.split()
            comp = analise[1]
            media += float(comp)
            temp_no = temp_no.getProx()
            cont += 1
        print(media/cont)


####################################################################################################
l = List()

while True:
    op = int(input('\n1)Cadastrar novo funcionário\n2)Excluir funcionário (a partir de um nome)\n3)O nome do '
                   'funcionário que tem o maior salário\n4)Media\n5)Sair: '))

    if op is 1:
        l.push()
    elif op is 2:
        l.exf()
    elif op is 3:
        l.sm()
    elif op is 4:
        l.med()
    elif op is 5:
        break
    else:
        print('Opc Invalida')
