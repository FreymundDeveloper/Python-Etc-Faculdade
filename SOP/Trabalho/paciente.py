import threading
import time

verifc = []  # Cria um vetor para receber os dados atuais e os dados que seram alterados no arquivo txt


def recuperar(cv):  # Cria a função recuperar(recupera os dados atuais do arquivo txt)
    with cv:
        cv.acquire()  # Bloqueia o acesso

        global verifc  # Trasforma o vetor verifc em um variavel global

        with open('agenda.txt', 'r') as arquivo:  # Le e armazena os dados do arquivo txt no vetor verifc
            for lista_completa in arquivo:
                verifc.append(lista_completa)

        cv.release()  # Libera o acesso


def agendar(cv, nome, hrr):  # Cria a função agendar(Verifica os dados informados pelos pacientes e compara com os
    # dados do vetor verifc(vetor arquivo txt) marcando ou não as consultas
    with cv:

        cv.wait()  # Gera um processo de espera que aguarda os dados atuais(thread atual) finalize sua execução e
        # notifique sua finalização, para que outros dados possam ser executados

        cv.acquire()  # Bloqueia o acesso

        global verifc  # Trasforma o vetor verific em um variavel global

        conf = []  # Cria um vetor para receber os dados q serão alterados pela função

        print('Tentando agendar consulta: %s às %s' % (nome, hrr))

        for e in verifc:
            base = e.split()  # Recebe e fatia dentro de um vetor a linha de dados atual do vetor que contem os dados
            # do arquivo txt
            analise = base[0] + ' ' + base[1]  # Armazena dentro de uma variavel o nome do medico e o horario atual da
            # linha de dados atual do vetor que contem os dados do arquivo txt

            # Verifica se o horario informado pelo paciente é igual ao horario da linha de dados atual do vetor verifc(
            # vetor arquivo txt)
            if hrr == base[1]:
                if base[2] == 'Disponivel':  # Verifica se a linha de dados atual do vetor verifc(vetor arquivo txt)
                    # está com status de "Disponivel"
                    conf.append(analise + ' ' + nome + '\n')  # Armazena os dados alterados no vetor conf(vetor com
                    # dados modificados)
                    print('Agendado!')
                else:
                    conf.append(e)  # Armazena os dados atuais do vetor verifc(vetor arquivo txt) no vetor conf(vetor
                    # com dados modificados)
                    print('Horário ocupado!')
            else:
                conf.append(e)  # Armazena os dados atuais do vetor verifc(vetor arquivo txt) no vetor conf(vetor com
                # dados modificados)

        verifc = conf.copy()  # Copia os dados do vetor conf para o vetor verifc

        cv.release()  # Libera o acesso


def salvar(cv):  # Cria a função salvar(atualiza os dados do arquivo txt)
    with cv:
        cv.acquire()  # Bloqueia o acesso

        global verifc  # Trasforma o vetor verifc em um variavel global

        with open('agenda.txt', 'w') as convercao:  # Insere os dados do vetor verfc no arquivo txt
            for c in verifc:
                convercao.write(str(c))
            convercao.close()

        cv.release()  # Libera o acesso


print('Agendando consultas...')

condition = threading.Condition()  # Cria uma variável de condição

# Entra com os dados necessarios nas threads recover que executa a função recupera e save que executa a função
# salvar
recover = threading.Thread(name='recover', target=recuperar, args=(condition,))
save = threading.Thread(name='save', target=salvar, args=(condition,))

# Entra com os dados e incicializa as threads
paciente1 = threading.Thread(target=agendar, args=(condition, 'Paulo', '13:00',))
paciente2 = threading.Thread(target=agendar, args=(condition, 'Davi', '13:00',))
paciente3 = threading.Thread(target=agendar, args=(condition, 'Rodrigo', '9:00',))
paciente4 = threading.Thread(target=agendar, args=(condition, 'Antonio', '16:00',))
paciente5 = threading.Thread(target=agendar, args=(condition, 'Ana', '12:00',))
paciente6 = threading.Thread(target=agendar, args=(condition, 'Godofredo', '9:00',))
paciente7 = threading.Thread(target=agendar, args=(condition, 'Leo', '15:00',))
paciente8 = threading.Thread(target=agendar, args=(condition, 'Luisa', '8:00',))
paciente9 = threading.Thread(target=agendar, args=(condition, 'Pedrinho', '12:00',))
paciente10 = threading.Thread(target=agendar, args=(condition, 'Laira', '11:00',))

recover.start()
recover.join()

paciente1.start()
time.sleep(1)
paciente2.start()
time.sleep(1)
paciente3.start()
time.sleep(1)
paciente4.start()
time.sleep(1)
paciente5.start()
time.sleep(1)
paciente6.start()
time.sleep(1)
paciente7.start()
time.sleep(1)
paciente8.start()
time.sleep(1)
paciente9.start()
time.sleep(1)
paciente10.start()
time.sleep(1)

condition.acquire()  # Bloqueia o acesso

condition.notifyAll()  # Quebra o processo de espera gerado pelo comando "wait()"

condition.release()  # Libera o acesso

paciente1.join()
paciente2.join()
paciente3.join()
paciente4.join()
paciente5.join()
paciente6.join()
paciente7.join()
paciente8.join()
paciente9.join()
paciente10.join()

save.start()
save.join()
