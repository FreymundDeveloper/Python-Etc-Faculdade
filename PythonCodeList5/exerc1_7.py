def f(n):
    if n == 0:
        return 0
    if n >= 1:
        return n + f(n - 1)


n=int(input('Digite um valor:'))
print(f(n))
