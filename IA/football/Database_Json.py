import json

class Database_Json():
    __FileName=None
    __Data=None

    def __init__(self, Name):
        if(Name != None):
            self.__FileName = Name

    def load_Data(self):
        with open(self.__FileName, 'r') as json_file:
            self.__Data = json.load(json_file)

    def get_Data(self):
        return(self.__Data)

    def get_Database_Name(self):
        for key in self.__Data:
            return(key)

    def toString(self):
        name = self.get_Database_Name()
        result = ''
        for time in self.__Data[name]:
            nome = time['nome']
            titulos = time['titulos']
            estado  = time['estado']
            cidade = time['cidade']
            cores = time['cores']
            result += 'nome=%s    titulos=%s    estado=%s    cidade=%s    cores=%s\n' % (nome, titulos, estado, cidade, cores)
        return(result)
