op=0

while op !=5:
    op=float(input('1)Adição;\n2)Subtração;\n3)Divisão;\n4)Multiplicação;\n5)Sair;'))

    if op==1:
        rsp=float(input('Digite um numero:'))

        n=1

        while n <= 10:
            print(n,'+', rsp,'=', n+rsp)
            n=n+1

    elif op==2:
        rsp=float(input('Digite um numero:'))

        n=1

        while n <= 10:
            print(n,'-', rsp,'=', n-rsp)
            n=n+1

    elif op==3:
        rsp=float(input('Digite um numero:'))

        n=1

        while n <= 10:
            print(n,':', rsp,'=', n/rsp)
            n=n+1

    elif op==4:
        rsp=float(input('Digite um numero:'))

        n=1

        while n <= 10:
            print(n,'X', rsp,'=', n*rsp)
            n=n+1
