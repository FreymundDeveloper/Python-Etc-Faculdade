n = 0
mt=0
ms=0

while n < 5:
    no1 = float(input('Digite a nota 1 do aluno: '))
    no2 = float(input('Digite a nota 2 do aluno :'))

    med=(no1+no2)/2

    if med >= 7:
        ms +=1

    print('Media:', med)

    mt=mt+med

    n +=1

mt=mt/5

print('Media da turma: %.f;\n Alunos com media <= 7: %.f' % (mt, ms))
