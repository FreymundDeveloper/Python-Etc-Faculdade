def v(n, inc, t):

    if inc is not n:
        t += str(inc) + ' '
        print(t)
        v(n, inc + 1, t)
    else:
        t += str(inc) + ' '
        print(t)
        return

inc=1
t=''
n=int(input('Digite um valor:'))
v(n,inc,t)
