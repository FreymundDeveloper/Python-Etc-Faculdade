class No_fila:
    def __init__(self):
        self.__nome = None
        self.__proximo = None

    def set_nome(self, nome):
        self.__nome = nome

    def set_proximo(self, proximo):
        self.__proximo = proximo

    def get_nome(self):
        return self.__nome

    def get_proximo(self):
        return self.__proximo


class Fila:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def push(self, nome):  # Lembrese seu desgraçado, uma entrada só ocorre quando a função é chamada
        new = No_fila()
        if new:
            new.set_nome(nome)
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

    def print_all(self):
        if self.__final:
            saida = "Fila: \n"
            temp = self.__inicio
            while temp:
                saida += temp.get_nome() + "\t"
                temp = temp.get_proximo()
            print(saida)
        else:
            print("Fila vazia.")

    def print_next(self):
        if self.__inicio:
            temp = self.__inicio
            print("Primeiro elemento na fila: ", temp.get_nome())
        else:
            print("Fila vazia.")

    def pop_all(self):
        if self.__final:
            temp = self.__inicio
            while temp:
                if self.__inicio:
                    self.__inicio = self.__inicio.get_proximo()
                    temp = self.__inicio
                    if not self.__inicio:
                        self.__final = None
                        self.__inicio = None
        else:
            print("Fila vazia.")


def main():
    fila = Fila()
    while True:
        op = int(input("1 Incluir nome. \n" +
                       "2 Excluir/Atender próximo. \n" +
                       "3 Imprimir todos da fila. \n" +
                       "4 Imprimir/Verificar quem é o primeiro. \n" +
                       "5 Limpar fila. \n" +
                       "6 Sair. \n"))
        if op is 1:
            nome = input("Informe um nome:\n")
            fila.push(nome)
        elif op is 2:
            fila.pop()
        elif op is 3:
            fila.print_all()
        elif op is 4:
            fila.print_next()
        elif op is 5:
            fila.pop_all()
        elif op is 6:
            break
        else:
            print("Opcao invalida.")


if __name__ == '__main__':
    main()
