op=str
c=0
qdm=0

while op != 'fim':
    op=input('Digite se o individuo é homem(M) ou mulher(F):')

    if op == 'F':
        qdm=qdm+1

    c=c+1

print(' %.f mulheres foram digitadas' % qdm)
