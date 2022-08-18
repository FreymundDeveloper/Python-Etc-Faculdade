v = [34, 2, 1, 22, 14, 5]
v2 = []
x = len(v) - 1
maiorvalor = v[x]
menorvalor = v[x]
result = None
c = True
verf = None

while x >= 0:
    y = len(v) - 1

    while y >= 0:
        if c:
            if v[y] > maiorvalor:
                maiorvalor = v[y]

            if v[y] < menorvalor:
                menorvalor = v[y]

        elif maiorvalor > v[y] >= verf:
            result = v[y]
            verf = v[y]

        y -= 1

    if not c:
        maiorvalor = result

    y = -1
    for i in v:
        if i == maiorvalor:
            y += 1

    if y > 0:
        x -= y

    while y >= 0:
        v2.append(maiorvalor)
        y -= 1

    verf = menorvalor
    c = False
    x -= 1
