n=[]
x=0

c=int(input('Quantos valores deseja digitar:'))

while x < c:
    n.append(int(input('Digite um valor:')))
    x += 1

f=len(n)
while f > 1:
    t=False
    x=0
    while x < (f-1):
        if n[x] > n[x+1]:
            aux=n[x]
            n[x]=n[x+1]
            n[x+1]=aux
            t=True
        x += 1
    if not t:
        break
    f -= 1
for e in n:
    print(e)
