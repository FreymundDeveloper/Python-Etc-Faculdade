import math

a=float(input('De um valor ao A:'))
b=float(input('De um valor ao B:'))
c=float(input('De um valor ao C:'))

delta=(b**2)-(4*a*c)
d=math.sqrt(delta)
x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)

print('A raiz desta euquação é S={ %.f , %.f }' % (x1, x2))
