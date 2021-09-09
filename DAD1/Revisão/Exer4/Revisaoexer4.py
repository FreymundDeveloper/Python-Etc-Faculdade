class STR:
    _st = None

    def __init__(self):
        self._st = []

    def __del__(self):
        self._st = None

    def si(self, l):
        self._st = l

    def ial(self, strg):
        self._st.append(strg)

    def gi(self):
        return self._st

    def filt(self, lt):
        lst = []
        for x in self._st:
            if x[0].lower() == lt.lower():
                lst.append(x)
        return lst

    def oc(self):
        f = len(self._st)
        while f > 1:
            t = False
            x = 0
            while x < (f - 1):
                if self._st[x] > self._st[x + 1]:
                    aux = self._st[x]
                    self._st[x] = self._st[x + 1]
                    self._st[x + 1] = aux
                    t = True
                x += 1
            if not t:
                break
            f -= 1
        return self._st

    def od(self):
        f = len(self._st)
        while f > 1:
            t = False
            x = 0
            while x < (f - 1):
                if self._st[x] < self._st[x + 1]:
                    aux = self._st[x]
                    self._st[x] = self._st[x + 1]
                    self._st[x + 1] = aux
                    t = True
                x += 1
            if not t:
                break
            f -= 1
        return self._st
