from exercREV import Pessoa, Prof, ProfUN, AlunoUN, Aluno

obj = []
obj.append(Pessoa('Red', 1111))
obj.append(Prof('Rudimir', 2222, 'Vagabundagem'))
obj.append(Prof('Varelo', 1212, 'Dorme'))
obj.append(Aluno('Feder', 3333, 1234))
obj.append(ProfUN('Doviar', 4444, 'nenhuma', 'sabe de nada', 2345))
obj.append(AlunoUN('Cledinei', 5555, 3456, 'politico'))
obj.append(AlunoUN('Rock', 5656, 4567, 'Crosfiteiro'))

for x in obj:
    print(x.setn(), '-', x.setcpf())
