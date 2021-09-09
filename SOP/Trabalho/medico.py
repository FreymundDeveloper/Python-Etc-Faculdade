import threading


def marcar_disp(cv, comp):  # Cria a classe marcar_disp(Marca a disponibilidade do medico)
    with cv:

        cv.acquire()  # Bloqueia o acesso

        dd = open('agenda.txt', 'r')  # Abre e le o arquivo txt onde serão armazenados os dados
        lista = dd.readlines()  # Armazena os dados já existentes do arquivo em um string
        dd.close()  # Fecha o arquivo txt
        verificar = False  # Cria um verificador para variaveis de condição mais simples
        verificar2 = False  # Cria um verificador para variaveis de condição mais complexas

        if len(lista) == 10:  # Verifica atraves do vetor se o arquivo txt ainda não esta cheio
            print('Lista cheia')

        else:
            for e in lista:
                analise = e.split()  # Recebe e fatia dentro de um vetor a linha de dados atual do vetor que contem os
                # dados do arquivo txt
                horario_analise = comp.split()  # Recebe e fatia dentro de um vetor os dados informados pelo medico

                # Analisa se os dados do vetor(arquivo txt) e os dados do usuario(medico) são completamente iguais
                if analise[0] == horario_analise[0] and analise[1] == horario_analise[1]:
                    verificar2 = True

                elif analise[0] == horario_analise[0]:  # Verifica se o nome do trecho atual do vetor é igual ao do
                    # medico
                    analise_detalhada = analise[1]  # Recebe e fatia dentro de um vetor o horario na linha atual do
                    # vetor
                    h_a_detalhada = horario_analise[1]  # Recebe e fatia dentro de um vetor o horario informado pelo
                    # medico

                    # Nas linhas seguintes, os horarios tanto do vetor(arquivo txt) quanto do medico(usuario) são
                    # dividos em "hora e minutos"
                    analise_conflito_hora = int(analise_detalhada[0:2])
                    analise_conflito_mnt = int(analise_detalhada[3:5])
                    h_a_conflito_hora = int(h_a_detalhada[0:2])
                    h_a_conflito_mnt = int(h_a_detalhada[3:5])

                    # As duas verificações a seguir verificam se o horario informado pelo medico(usuario) não entrara em
                    # conflito com outro horario já marcado por ele mesmo, dentro do vetor(arquivo txt)
                    if analise_detalhada[0:2] == h_a_detalhada[0:2] and analise_detalhada[3:5] != h_a_detalhada[3:5]:
                        verificar2 = True

                    elif h_a_conflito_hora < analise_conflito_hora and h_a_conflito_mnt > analise_conflito_mnt:
                        verificar2 = True

                    else:  # Adiciona o horario de disponibilidade ao arquivo txt
                        with open('agenda.txt', 'a') as arquivo:
                            arquivo.write('\n' + str(comp) + ' Disponivel')
                            verificar2 = True

                else:
                    verificar = True

            if verificar is True and verificar2 is False:  # Adiciona o horario de disponibilidade ao arquivo txt,
                # apenas se o verificador simples(verificar) tenha sido alterado e o verificador complexo(verificador2)
                # tenha se mantido intacto
                with open('agenda.txt', 'a') as arquivo:
                    arquivo.write('\n' + str(comp) + ' Disponivel')

        cv.release()  # Libera o acesso


def reset():  # Reseta os horarios de disponibilidade marcados no arquivo txt
    with open('agenda.txt', 'w') as arquivo:
        arquivo.write(str('LISTA DE HORARIOS') + '\n' + str('Medico / Horario / Paciente'))
        print('Lista de horarios resetada')


while True:  # Cria um loop de repetição com os dados abaixo
    op = int(input('1)Entrada de dados;\n2)Reset;\n3)Sair\nOpç: '))
    if op == 1:  # Entra com os dados e incicializa as threads
        condition = threading.Condition()  # Cria uma variavel de condição

        medico1 = threading.Thread(target=marcar_disp, args=(condition, 'Dr.Luis 13:00',))
        medico2 = threading.Thread(target=marcar_disp, args=(condition, 'Dr.Diego 9:00',))
        medico3 = threading.Thread(target=marcar_disp, args=(condition, 'Dra.Sara 16:00',))
        medico4 = threading.Thread(target=marcar_disp, args=(condition, 'Dra.Augusta 19:00',))
        medico5 = threading.Thread(target=marcar_disp, args=(condition, 'Dr.Pedro 8:00',))
        medico6 = threading.Thread(target=marcar_disp, args=(condition, 'Dra.Salomena 15:00',))
        medico7 = threading.Thread(target=marcar_disp, args=(condition, 'Dra.Podvisc 12:00',))
        medico8 = threading.Thread(target=marcar_disp, args=(condition, 'Dra.Lindi 11:00',))

        medico1.start()
        medico1.join()
        medico2.start()
        medico2.join()
        medico3.start()
        medico3.join()
        medico4.start()
        medico4.join()
        medico5.start()
        medico5.join()
        medico6.start()
        medico6.join()
        medico7.start()
        medico7.join()
        medico8.start()
        medico8.join()

    elif op == 2:  # Reseta o arquivo txt
        reset()
    elif op == 3:  # encerra o loop de repetição
        break
    else:
        print('Invalido')
