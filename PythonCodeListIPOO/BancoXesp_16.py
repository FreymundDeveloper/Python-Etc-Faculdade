from BancoX import Bank, BankEsp


c = BankEsp(None, None, None, 50)
a = 0
while a != 2:
    a = int(input('1)Criar usuario; \n2)Sair;'))
    if a is 1:
        c.rusuario(input('Digite o seu nome:'))
        c.rconta(float(input('Digite o valor do seu saldo:')))
        c.rtel(input('Digite o seu telefone:'))
        z = 0
        while z != 5:
            z = int(input('1)Para sacar;\n2)Para depositar;\n3)Exibir dados;\n4)Exibir extrato;\n5)Sair;'))
            if z is 1:
                c.sacar(float(input('Digitar valor a sacar:')))
            if z is 2:
                c.depositar(float(input('Digite o valor a depositar')))
            if z is 3:
                print(c.dados())
            if z is 4:
                c.extr()
