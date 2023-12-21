def f(a, b, c=2):
    while c < v:

        aux = a
        a = b
        b = aux + b
        c += 1

    return a+b


a = 0
b = 1
v = int(input('Digite uma possição:'))

print(f(a,b))
