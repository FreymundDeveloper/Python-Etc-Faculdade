t=[-10, -8, 0, 1, 2, 3, -2, -4]
x=0
ma=t[0]
me=t[0]
vt=0

while x < len(t):
    if t[x] < ma:
        ma=t[x]
    if t[x] > me:
        me=t[x]

    vt=vt + t[x]
    x += 1

print('Maior=',me)
print('Menor=',ma)
print('Media=',vt/len(t))
