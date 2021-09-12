from exercCDC21 import Div, Mul, Soma, Sub

x = 0
while x != 5:
    x = int(input('1)Div \n2)Mul \n3)Soma \n4)Sub \n5)Sair \nSelecione:'))
    if x is 1:
        z = Div(None, None)
        z.ajustv(float(input('Digite o valor:')), float(input('Digite o valor:')))
        print(z.cal())

    if x is 2:
        z = Mul(None, None)
        z.ajustv(float(input('Digite o valor:')), float(input('Digite o valor:')))
        print(z.cal())

    if x is 3:
        z = Soma(None, None)
        z.ajustv(float(input('Digite o valor:')), float(input('Digite o valor:')))
        print(z.cal())

    if x is 4:
        z = Sub(None, None)
        z.ajustv(float(input('Digite o valor:')), float(input('Digite o valor:')))
        print(z.cal())
