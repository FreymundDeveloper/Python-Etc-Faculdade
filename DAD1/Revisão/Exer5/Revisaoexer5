from Revisão.Exer5.Revisaoexer5 import CDB

v = CDB()
x = 0
chave = False

while x is not 3:
    x = int(input(' 1)Cadastro;\n 2)Avaliação;\n 3)Sair:'))

    if x is 1:
        n = int(input('Digite o numero de participantes:'))
        z = 0
        i = []
        a = []
        p = []
        chave = True
        while z < n:
            i.append(input('Digite o seu nome:'))
            a.append(float(input('Digite o sua altura:')))
            p.append(float(input('Digite seu peso:')))
            v.cadastro(i, a, p)
            z += 1
    if x is 2:
        v.aval()

    elif chave is False:
        print('OPÇ 1 NECESSARIA')
