op=0
ma=-99999.9
me=99999.9

while op != -123:
    op=float(input('Digite um valor:'))

    if op > ma and op!=-123:
        ma=op

    elif op < me and op!=-123:
        me=op

print('Maior= %.f;\nMenor= %.f.' % (ma, me))
