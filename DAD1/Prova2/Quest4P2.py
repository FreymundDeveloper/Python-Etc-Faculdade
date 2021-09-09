class No_fila:
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


class Minha_fila:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def push(self, inteiro):

        new = No_fila()
        if new:
            new.set_inteiro(inteiro)
            if self.__final:
                self.__final.set_proximo(new)
                self.__final = new
            else:
                self.__inicio = self.__final = new

    def pop(self):

        if self.__inicio:
            self.__inicio = self.__inicio.get_proximo()
            if not self.__inicio:
                self.__final = None
        else:
            print("Fila vazia.")

    def imprime_divisiveis(self):
        if self.__final:
            saida = []
            temp = self.__inicio
            count = 0
            while temp:
                count += 1
                temp = temp.get_proximo()

            temp = self.__inicio

            while temp:
                if temp.get_inteiro() % count == 0:
                    saida.append(str(temp.get_inteiro()))
                temp = temp.get_proximo()
            print(saida)
        else:
            print("Fila vazia.")


def main():
    fila = Minha_fila()
    while True:
        op = int(input("1 - Incluir inteiro na fila.\n" +
                       "2 – Excluir inteiro da fila​.\n" +
                       "3 – Imprimir valores divisíveis pela quantidade de elementos​.\n" +
                       "4 – Sair."))
        if op is 1:
            fila.push(int(input('digite valor:')))
        elif op is 2:
            fila.pop()
        elif op is 3:
            fila.imprime_divisiveis()
        elif op is 4:
            exit()
        else:
            print("Opcao invalida.")


if __name__ == '__main__':
    main()
