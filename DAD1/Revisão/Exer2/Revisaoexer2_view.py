from Revisão.Exer2.Revisaoexer2 import Calculadora

x = 0
a = Calculadora(None, None)
chave = False

while x is not 6:
    x=int(input('1)Digitar valores;\n2)Soma;\n3)Subtrasão;\n4)Multiplicasão;\n5)Divisão;\n6)Sair:'))

    if x is 1:
        a.lervalorA(int(input('Digite o valor A:')))
        a.lervalorB(int(input('Digite o valor B:')))
        chave = True

    elif x is not 1 and chave is False:
        print('OP 1 necessaria')

    if x is 2 and chave is True:
        print(a.soma())

    if x is 3 and chave is True:
        print(a.subtrasao())

    if x is 4 and chave is True:
        print(a.multiplicar())

    if x is 5 and chave is True:
        print(a.divisao())
