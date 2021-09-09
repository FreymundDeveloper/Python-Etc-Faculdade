class Medico:

    def __init__(self):
        self.__count = 0

    def marcar_disp(self):
        with open('agenda.txt', 'r') as arquivo:
            for lista_completa in arquivo:
                print(lista_completa)
                self.__count += 1

        if self.__count < 10:
            dd = open('agenda.txt', 'r')
            lista = dd.readlines()
            verificar = False
            verificar2 = False
            comp = input('\nDigite o nome e horario de disponibilidade:')
            conferir = comp.split()
            if len(conferir) != 2:
                print('Nome e horario PFV')
                return

            for e in lista:
                analise = e.split()
                horario_analise = comp.split()

                if analise[0] == horario_analise[0] and analise[1] == horario_analise[1]:
                    print('Dr', horario_analise[0], 'vc já tem uma marcação nesse horario.')
                    verificar2 = True

                elif analise[0] == horario_analise[0]:
                    analise_detalhada = analise[1]
                    h_a_detalhada = horario_analise[1]

                    analise_conflito_hora = int(analise_detalhada[0:2])
                    analise_conflito_mnt = int(analise_detalhada[3:5])
                    h_a_conflito_hora = int(h_a_detalhada[0:2])
                    h_a_conflito_mnt = int(h_a_detalhada[3:5])

                    if analise_detalhada[0:2] == h_a_detalhada[0:2] and analise_detalhada[3:5] != h_a_detalhada[3:5]:
                        print('Dr', horario_analise[0], 'vc já tem uma marcação durante esse horario.')
                        verificar2 = True

                    elif h_a_conflito_hora < analise_conflito_hora and h_a_conflito_mnt > analise_conflito_mnt:
                        print('Dr', horario_analise[0], 'esse horario vai conflitar com outro')
                        verificar2 = True

                    else:
                        with open('agenda.txt', 'a') as arquivo:
                            arquivo.write('\n' + str(comp) + ' Disponivel')
                            print('Horario de disponibilidade marcado Dr', analise[0])
                            verificar2 = True

                else:
                    verificar = True

            dd.close()
            if verificar is True and verificar2 is False:
                with open('agenda.txt', 'a') as arquivo:
                    arquivo.write('\n' + str(comp) + ' Disponivel')
                    print('Horario de disponibilidade marcado com sucesso')

        else:
            print('\nLISTA CHEIA')


s = Medico()

s.marcar_disp()
