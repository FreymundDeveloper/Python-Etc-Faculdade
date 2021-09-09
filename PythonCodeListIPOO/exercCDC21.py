class CDC:
    _v1 = None
    _v2 = None

    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2

    def __del__(self):
        self._v1 = None
        self._v2 = None

    def ajustv(self, v1, v2):
        self._v1 = v1
        self._v2 = v2


class Div(CDC):

    def __init__(self, v1, v2):
        super().__init__(v1, v2)

    def cal(self):
        return self._v1 / self._v2


class Mul(CDC):

    def __init__(self, v1, v2):
        super().__init__(v1, v2)

    def cal(self):
        return self._v1 * self._v2


class Soma(CDC):

    def __init__(self, v1, v2):
        super().__init__(v1, v2)

    def cal(self):
        return self._v1 + self._v2


class Sub(CDC):

    def __init__(self, v1, v2):
        super().__init__(v1, v2)

    def cal(self):
        return self._v1 - self._v2


