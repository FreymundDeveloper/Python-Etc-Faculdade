v = [2, 1, 5, 4, 3]
fim=len(v)

while fim > 1:
    t=False
    x=0
    while x < (fim-1):
        if v[x] < v[x+1]:
            aux=v[x]
            v[x]=v[x+1]
            v[x+1]=aux
            t=True
        x +=1
    if not t:
        break
    fim -= 1
for e in v:
    print(e)
