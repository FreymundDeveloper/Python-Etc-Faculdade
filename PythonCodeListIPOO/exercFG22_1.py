from exercFG22 import Retangulo, Quadrado, Triangulo, Circulo

x1 = 0
while x1 != 5:
    x1 = int(input('1)Retangulo;\n2)Quadrado;\n3)Triangulo;\n4)Circulo;\n5)Sair:\n'))
    if x1 is 1:
        f = Retangulo(None, None)
        x2 = 0
        while x2 != 3:
            x2 = int(input('1)Area;\n2)Perimetro;\n3)Sair\n'))
            if x2 is 1:
                print(f.ca())
            elif x2 is 2:
                print(f.cp())

    if x1 is 2:
        f = Quadrado(None, None)
        x2 = 0
        while x2 != 3:
            x2 = int(input('1)Area;\n2)Perimetro;\n3)Sair\n'))
            if x2 is 1:
                print(f.ca())
            elif x2 is 2:
                print(f.cp())

    if x1 is 3:
        f = Triangulo(None, None)
        x2 = 0
        while x2 != 3:
            x2 = int(input('1)Area;\n2)Perimetro;\n3)Sair\n'))
            if x2 is 1:
                print(f.ca())
            elif x2 is 2:
                print(f.cp())

    if x1 is 4:
        f = Circulo(None, None)
        x2 = 0
        while x2 != 3:
            x2 = int(input('1)Area;\n2)Perimetro;\n3)Sair\n'))
            if x2 is 1:
                print(f.ca())
            elif x2 is 2:
                print(f.cp())
