v1 = []
v2 = []
v3 = []
x = 0
x2 = 0
x3 = 0

c = int(input('Numeros a digitar:'))

while x < c:
    v1.append(int(input('Digite:')))
    v2.append(int(input('Digite:')))
    x += 1

z2=0
x = 0

while x < c and v1 != []:
    while x2 <= x:
        if v1[x2] is v2[x]:
            del v1[x]
            break
        else:
            x += 1
        x2 += 1
    x2=0
    z2 +=1

z=0

while z < z2:
    if v1 != []:
        v3.append(v1[x3])
        z += 1
    v3.append(v2[x3])
    z += 1
    x3 += 1

print(v3)
