v=[]
x=0
p=99999.9

c=int(input('Quantos valores deseja digitar:'))

while x < c:
    v.append(float(input('Digite um valor:')))
    x += 1

x=0

while x < len(v):
    if v[x] < p:
        p=v[x]

    x += 1

print('O menor valor é:',p)
