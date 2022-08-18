from Revisão.Exer7.Revisaoexer7 import CDC

v = CDC()
x = 0

while x is not 5:
    x = int(input('1)Gabarito; \n2)Alunos, respostas e Resultados;'))

    if x is 1:
        g = []
        z = 0
        while z < 5:
            g.append(input('Digite o gabarito, resposta %.i :' % (z + 1)))
            z += 1
        v.gabt(g)

    if x is 2:
        z = False
        m = []
        r = []
        while z is not True:
            z = input('Digite sua matricula(E para sair):')
            if z is 'E':
                z = True
            else:
                m.append(z)
                y = 0
                while y < 5:
                    r.append(input('Digite sua resposta(questão %.i):' % (y+1)))
                    y += 1
        v.an(m, r)








