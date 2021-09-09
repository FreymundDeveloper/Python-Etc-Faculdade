class Menu:
    _listA = None
    _listB = None

    def __init__(self):
        self._listA = None
        self._listB = None

    def __del__(self):
        self._listA = None
        self._listB = None

    def receb(self, n):
        self._listA = n

    def ord(self):
        f = len(self._listA)
        while f > 1:
            t = False
            x = 0
            while x < (f - 1):
                if self._listA[x] > self._listA[x + 1]:
                    tempo = self._listA[x]
                    self._listA[x] = self._listA[x + 1]
                    self._listA[x + 1] = tempo
                    t = True
                x += 1
            if not t:
                break
            f -= 1
        for e in self._listA:
            print(e)

    def rep(self):
        x = 0
        a = 0

        while x < len(self._listA):
            z = 0
            q = 0
            y = x
            c = False

            while z < len(self._listA):
                if self._listA[x] is self._listA[z]:
                    a = self._listA[x]
                    q += 1
                z += 1

            while y > 0:
                if a is self._listA[y - 1]:
                    c = False
                    break
                else:
                    c = True
                y -= 1
            if c is True and q > 1:
                print(a, q)

            if x is 0 and q > 1:
                print(a, q)
            x += 1

    def elim(self):
        x = 0
        a = 0
        self._listB = []

        while x < len(self._listA):
            z = 0
            q = 0
            y = x
            c = False

            while z < len(self._listA):
                if self._listA[x] is self._listA[z]:
                    a = self._listA[x]
                    q += 1
                z += 1

            while y > 0:
                if a is self._listA[y - 1]:
                    c = False
                    break
                else:
                    c = True
                y -= 1
            if c is True and q > 1:
                self._listB.append(a)

            if x is 0 and q > 1:
                self._listB.append(a)
            x += 1
        print(self._listB)

    def med(self):
        x = 0
        med = 0
        while x < len(self._listA):
            med = med + self._listA[x]
            x += 1

        print(med/len(self._listA))
