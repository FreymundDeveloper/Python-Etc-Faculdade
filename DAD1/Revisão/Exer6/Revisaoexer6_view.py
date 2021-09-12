from Revisão.Exer6.Revisaoexer6 import UN

v = UN()
x = None
chave = False

while x is not 5:
    x = int(input('1) Leia as informações de cada aluno;\n'
                  '2) Imprima a relação dos alunos aprovados;\n'
                  '3) Imprima a relação dos alunos em exame;\n'
                  '4) Determine e imprima o melhor aluno e o aluno com menor média;\n'
                  '5)Sair:'))

    if x is 1:
        z = None
        n = []
        s = []
        n1 = []
        n2 = []
        for e in n, s, n1, n2:
            z = input('Digite o numero da matricula(E para sair):')
            if z is 'E':
                break
            else:
                n.append(z)
                s.append(input('Digite o sexo:'))
                n1.append(float(input('Digite a primeira nota:')))
                n2.append(float(input('Digite a segunda nota:')))
                v.inf(n, s, n1, n2)
                chave = True

    if x is 2 and chave is True:
        v.ap()

    if x is 3 and chave is True:
        v.exa()

    if x is 4 and chave is True:
        v.mm()
