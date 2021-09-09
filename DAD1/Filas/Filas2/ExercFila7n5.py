class No:
    def __init__(self):
        self.__inteiro = 0
        self.__proximo = None

    def set_inteiro(self, inteiro):
        self.__inteiro = inteiro

    def set_proximo(self, proximo):
        self.__proximo = proximo

    def get_inteiro(self):
        return self.__inteiro

    def get_proximo(self):
        return self.__proximo


class Pilha:
    def __init__(self):
        self.__topo = None

    def push(self, inteiro):
        temp = No()
        if temp:
            temp.set_inteiro(inteiro)
            temp.set_proximo(self.__topo)
            self.__topo = temp

    def get_top(self):
        if self.__topo:
            return self.__topo.get_inteiro()

    def pop_top(self):
        if self.__topo:
            self.__topo = self.__topo.get_proximo()
        else:
            print("Pilha vazia.")


class Fila:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def push(self, inteiro):
        new = No()
        if new:
            new.set_inteiro(inteiro)
            if self.__final:
                self.__final.set_proximo(new)
                self.__final = new
            else:
                self.__inicio = self.__final = new

    def print_all(self):
        if self.__final:
            saida = "Fila:\t"
            temp = self.__inicio
            while temp:
                saida += str(temp.get_inteiro()) + "\t"
                temp = temp.get_proximo()
            print(saida)
        else:
            print("Fila vazia.")

    def pop_all(self):
        if self.__final:
            temp = self.__inicio
            while temp:
                self.__inicio = self.__inicio.get_proximo()
                temp = self.__inicio
                if not self.__inicio:
                    self.__final = None
                    self.__inicio = None
        else:
            print("Fila vazia.")

    def pop(self):
        if self.__inicio:
            self.__inicio = self.__inicio.get_proximo()
            if not self.__inicio:
                self.__final = None
        else:
            print("Fila vazia.")

    def print_first(self):
        if self.__final:
            temp = self.__inicio
            print("\nPrimeiro elemento = ", str(temp.get_inteiro()))
        else:
            print("Fila vazia.")

    def invert(self):
        if self.__final:
            pilha = Pilha()
            temp = self.__inicio

            while temp:
                inteiro = temp.get_inteiro()
                pilha.push(inteiro)
                temp = temp.get_proximo()

            self.pop_all()
            proximo = pilha.get_top()
            while proximo:
                proximo = pilha.get_top()
                if proximo is not None:
                    self.push(proximo)
                    pilha.pop_top()


def main():
    fila = Fila()
    while True:
        op = int(input("Opcoes:\n" +
                       "1 – Incluir inteiro na fila​.\n" +
                       "2 – Excluir inteiro da fila​.\n" +
                       "3 – Imprimir o primeiro inteiro da fila​.\n" +
                       "4 – Imprimir todos os inteiros da fila​.\n" +
                       "5 – Excluir todos os inteiros da fila​.\n" +
                       "6 – Inverter os inteiros da fila​.\n" +
                       "7 – Imprimir os inteiros pares e depois os inteiros ímpares​.\n"
                       "8 - Sair.\n"))

        if op is 1:
            inteiro = int(input("Informe inteiro pra enfileirar.\n"))
            fila.push(inteiro)
        elif op is 2:
            fila.pop()
        elif op is 3:
            fila.print_first()
        elif op is 4:
            fila.print_all()
        elif op is 5:
            fila.pop_all()
        elif op is 6:
            fila.invert()
        elif op is 8:
            break
        else:
            print("Opcao invalida.")


if __name__ == '__main__':
    main()