v = [15, 7, 27, 39]
x = 0
n1 = True
n2 = True

p = int(input('Qual valor deseja verificar:'))
c = int(input('Qual o outro:'))

while x < len(v):
    if v[x] is p:
        n1 = False
        print('P localizado na possição ', x)
    if v[x] is c:
        n2 = False
        print('C localizado na possição ', x)

    x += 1

if n1 == False and n2 == False:
    print('Valores localizados')
elif n1 == False and n2 == True:
    print('Apenas P localizado')
elif n1 == True and n2 == False:
    print('Apenas C localizado')
else:
    print('Nenhum valor localizado')
