from experta import *
from Database_Json import Database_Json

class Play_Experta_Cons(KnowledgeEngine):
    __MaiorId = None
    __FileName = None

    def __init__(self, Name=None):
        super().__init__()
        if(Name != None):
            self.__FileName = Name

    @DefFacts()
    def _initial_action(self):
        Base=Database_Json(self.__FileName)
        Base.load_Data()
        fut = Base.get_Database_Name()
        data = Base.get_Data()
        for time in data[fut]:
            nome = time['nome']
            titulos = time['titulos']
            estado  = time['estado']
            cidade = time['cidade']
            cores = time['cores']
            yield Fact(Database=fut, nome=nome, titulos=titulos, estado=estado, cidade=cidade, cores=cores)
        

    @Rule(Fact(Database='Futebol', nome=MATCH.nom, titulos=MATCH.tit, estado=MATCH.est, cidade=MATCH.cid, cores=MATCH.cor))
    def print_database(self, nom, tit, est, cid, cor):
        print('Futebol:    nome=%s    titulos=%s    estado=%s    cidade=%s    cores=%s' % (nom, tit, est, cid, cor))

    @Rule(Fact(Database='Futebol'),
          NOT(Fact(Maior='Maior')))
    def inicia_busca(self):
        self.__MaiorId=self.declare(Fact(Maior='Maior', equipe='Nenhuma', titulos='0'))
        

    @Rule(Fact(Database='Futebol', nome=MATCH.nom, titulos=MATCH.tit),
          Fact(Maior='Maior', equipe=MATCH.eqp, titulos=MATCH.num))
    def resultado_busca(self, nom, tit, num):
        titulos1 = int(tit)
        titulos2 = int(num)
        if(titulos1 > titulos2):
            self.retract(self.__MaiorId)
            self.__MaiorId = self.declare(Fact(Maior='Maior', equipe=nom, titulos=tit))

    @Rule(Fact(Maior='Maior', equipe=MATCH.eqp, titulos=MATCH.num))
    def fim_busca(self, eqp, num):
        print('Resultado da busca:')
        print('Equipe com maior número de títulos=%s' % eqp)
        print('Número de títulos=%s' % num)
