class Pessoa:

    _nome = None
    _cpf = None

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def __del__(self):
        self._nome = None
        self._cpf = None

    def getn(self, nome):
        self._nome = nome

    def getcpf(self, cpf):
        self._cpf = cpf

    def setn(self):
        return self._nome

    def setcpf(self):
        return self._cpf


class Prof(Pessoa):

    _area = None

    def __init__(self, nome, cpf, area):
        super().__init__(nome, cpf)
        self._area = area

    def geta(self, area):
        self._area = area

    def seta(self, area):
        return self._area


class ProfUN(Prof):

    _ies = None
    _matricula = None

    def __init__(self, nome, cpf, area, ies, matricula):
        super().__init__(nome, cpf, area)
        self._ies = ies
        self._matricula = matricula

    def geties(self, ies):
        self._ies = ies

    def getm(self, matricula):
        self._matricula = matricula

    def seties(self):
        return  self._ies

    def setn(self):
        return self._matricula


class Aluno(Pessoa):

    _matricula = None

    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self._matricula = matricula

    def getm(self, matricula):
        self._matricula = matricula

    def setm(self):
        return  self._matricula


class AlunoUN(Aluno):

    _curso = None

    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf, matricula)
        self._curso = curso

    def getc(self, curso):
        self._curso = curso

    def setc(self):
        return self._curso