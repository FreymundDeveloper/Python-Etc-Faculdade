class Cliente:

    def __init__(self):
        self.__verifc = []
        self.__conf = []

    def agendar(self):
        with open('agenda.txt', 'r') as arquivo:
            for lista_completa in arquivo:
                print(lista_completa)
                self.__verifc.append(lista_completa)

        opc = input('\nDigite o horario que deseja marcar(Medico+Hora):')
        chave = False
        verif = opc.split()
        if len(verif) != 2:
            print('Erro, digitalização incorreta')

        else:
            for e in self.__verifc:
                base = e.split()
                analise = base[0] + ' ' + base[1]

                if opc == analise:
                    if base[2] == 'Disponivel':
                        nome = input('Digite seu nome:')
                        self.__conf.append(analise + ' ' + nome + '\n')
                        print('Consulta agendada')
                        chave = True

                    else:
                        print('Indisponivel')
                        self.__conf.append(e)
                        chave = True

                else:
                    self.__conf.append(e)

            if not chave:
                print('Informações digitadas incompativeis com dados da lista de agendamentos')

            with open('agenda.txt', 'w') as convercao:
                for c in self.__conf:
                    convercao.write(c)


c = Cliente()
c.agendar()
