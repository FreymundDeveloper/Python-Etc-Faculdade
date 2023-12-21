def div(a, b):
    if a % b == 0:
        return True
    else:
        return False


a = float(input('Digite um numero:'))
b = float(input('Digite um numero:'))

print(div(a, b))
