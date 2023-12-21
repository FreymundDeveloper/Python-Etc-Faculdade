v=[15, 7, 27, 39]
x=0
n1=True
n2=True
n3=True
z=1

p=int(input('Digite o valor que vc quer localizar:'))
c=int(input('Digite outro valor:'))

while x < len(v):
    if v[x] is p:
        n1=False
        print('P encontrado ', z,'.')
        z += 1

    elif v[x] is c:
        n2=False
        print('C encontrado ', z,'.')
        z += 1

    if n1 == False and n2 == False:
        n3=False

    x +=1

if not n3:
    print('Valores encontrados')
elif n3:
    print('Outro valor não encontrado')
