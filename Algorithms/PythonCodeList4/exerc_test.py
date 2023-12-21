n=int(input('Quantas notas deseja digitar:'))
nt=[]
t=0
c=0

for x in range(0,n):
    nt.append(float(input('Digite uma nota:')))
    t=t+nt[x]
    c += 1

print('notas=', nt)
print('Media= %.2f ' % (t/c))
