def inv(n):
    s=' '
    while int(n)>0:
        r=int(n)%10
        s += str(r)
        n /= 10
    return s

n=int(input('nr'))
print('nr invertido:', inv(n))
