v=[]
c=0
md=0

while c < 5:
    v.append(float(input('Digite um numero:')))
    md=md+v[c]
    c += 1

print('Media=', md/5)
