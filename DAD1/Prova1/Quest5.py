class no_pilha:

    def __init__(self):
        self.__nome = None

        self.__idade = 0

        self.__prox = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, id):
        self.__idade = id

    def getProx(self):
        return self.__prox

    def setProx(self, prox):
        self.__prox = prox


class Pilha:

    def __init__(self):
        self.__topo = None

    def push(self):
        temp_no = no_pilha()

        if temp_no:
            temp_no.setNome(input('Digite seu nome: '))
            temp_no.setIdade(int(input('Digite sua idade: ')))
            temp_no.setProx(self.__topo)
            self.__topo = temp_no

    def pop(self):
        if self.__topo:
            self.__topo = self.__topo.getProx()

        else:
            print('Pilha vazia')

    def maiormenor(self):
        if self.__topo:

            temp_no = self.__topo.getProx()
            maior = self.__topo
            menor = self.__topo

            while temp_no:
                if temp_no.getIdade() > maior.getIdade():
                    maior = temp_no

                if temp_no.getIdade() < menor.getIdade():
                    menor = temp_no

                temp_no = temp_no.getProx()

            temp_no = self.__topo
            ma_nome = []
            me_nome = []

            while temp_no:
                if temp_no.getIdade() == maior.getIdade():
                    ma_nome.append(temp_no)
                if temp_no.getIdade() == menor.getIdade():
                    me_nome.append(temp_no)
                temp_no = temp_no.getProx()

            count = len(ma_nome) - 1
            result = '\nMaior: '

            while count >= 0:
                result += ('\n%s idade: %s' % (str(ma_nome[count].getNome()), str(maior.getIdade())))
                count -= 1

            count = 0
            result += '\nMenor'

            while count >= 0:
                result += ('\n%s idade: %s' % (str(me_nome[count].getNome()), str(menor.getIdade())))
                count -= 1

            print(result)

        else:
            print('Pilha vazia')

    def printall_media(self):
        if not self.__topo:
            print('Pilha vazia')

        else:
            temp = self.__topo
            tex = ''
            count = 0
            med = 0

            while temp:
                med += temp.getIdade()
                count += 1
                tex += ('\nNome: %s \nIdade: %s' % (str(temp.getNome()), str(temp.getIdade())))
                temp = temp.getProx()
            print(tex)
            print('Media: ', med / count)


p = Pilha()

while True:

    op = int(
        input("1-Empilhar\n2-Desempilhar\n3-Maior e menor idade\n4-Imprime todos e a Média das idades\n5-Sair\nOpção:"))

    if op is 1:

        p.push()

    elif op is 2:

        p.pop()

    elif op is 3:

        p.maiormenor()

    elif op is 4:

        p.printall_media()

    elif op is 5:

        break

    else:
        print('OPC invalida')
