op=0

while op !=9:
    op=float(input('1) soma;\n'
                   '2) subtração;\n'
                   '3) multiplicação;\n'
                   '4) divisão;\n'
                   '9) sair.\n'
                   'Digite uma opção:'))

    def resp():
        print('resulta ', rsp)

    if op == 1:
        n1=float(input('Digito um numero: '))
        n2=float(input('Digito um numero: '))
        rsp=n1+n2
        resp()

    elif op == 2:
        n1 = float(input('Digito um numero: '))
        n2 = float(input('Digito um numero: '))
        rsp=n1-n2
        resp()

    elif op == 3:
        n1 = float(input('Digito um numero: '))
        n2 = float(input('Digito um numero: '))
        rsp=n1*n2
        resp()

    elif op == 4:
        n1 = float(input('Digito um numero: '))
        n2 = float(input('Digito um numero: '))
        if n2 !=0:
            rsp=n1/n2
            resp()
        else:
            print('divsão por 0 invalida')
