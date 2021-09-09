# 2.1) Crie um arquivo (Extra: Usuário pode informar o nome do arquivo).
#
# 2.2) Solicite e permita inserir dados de cadastro de livros (Código, Título e Autor).
#
# 2.3) Apresente todos os registros cadastrados e permita buscar por código (Extra:
# Permita escolher busca sequencial ou binária - lembrem que para busca binária, o arquivo
# precisa estar ordenado. Extra_do_extra: Conte quantos códigos foram consultados antes de
# retornar o buscado.).
#
# 2.4) Adicione comentários didáticos, de forma que o código possa ser apresentado como
# exemplo de manipulação de arquivos e facilite a compreensão dos colegas.


class Livro:
    __cod = None
    __tit = None
    __autor = None
    __arquivo = None
    __nome = None

    def __init__(self):
        self.__cod = 0
        self.__tit = ''
        self.__autor = ''
        self.__arquivo = None
        self.__nome = None

    def criarArquivo(self):
        self.__nome = input('Qual o nome do arquivo: ')

        try:
            self.__arquivo = open('%s.txt' % self.__nome, 'r')

        except FileNotFoundError:
            self.__arquivo = open('%s.txt' % self.__nome, 'w')
            self.__arquivo.close()

            self.__arquivo = open('%s.txt' % self.__nome, 'r')

        self.__arquivo.close()

    def cadastrarLivro(self, c, t, a):
        self.__cod = str(c)
        self.__tit = str(t)
        self.__autor = str(a)

        cadastro = self.__cod + ' ' + self.__tit + ' ' + self.__autor
        analise = cadastro.split()
        abrir = self.apresentarRegistro()
        chave = False

        self.__arquivo = open('%s.txt' % self.__nome, 'a')

        if abrir == 'Registro vazio':
            chave = True

        else:
            for dado in abrir:
                analise_registro = dado.split()

                if analise_registro[0] == analise[0]:
                    print('Codigo ja existente')
                    chave = False
                    break

                else:
                    chave = True

        if chave is True:
            self.__arquivo.write(str(cadastro) + '\n')

        self.__arquivo.close()

    def apresentarRegistro(self):
        self.__arquivo = open('%s.txt' % self.__nome, 'r')
        lista_de_dados = []

        while True:
            linha = self.__arquivo.readline()

            if linha:
                lista_de_dados.append(linha)

            else:
                break

        self.__arquivo.close()

        if not lista_de_dados:
            return 'Registro vazio'

        else:
            return lista_de_dados

    def ordenar(self):
        lista = self.apresentarRegistro()  # Começa ordenação
        ordenar = []

        for dados in lista:
            if dados is not 'Registro vazio':
                verif = dados.split()
                ordenar.append(int(verif[0]))
            else:
                print('Registro vazio')

        if ordenar:
            certo = sorted(ordenar)
            lista_ordenada = []

            for dados1 in certo:
                for dados2 in lista:
                    comparar = dados2.split()
                    if int(comparar[0]) is dados1:
                        lista_ordenada.append(dados2)  # finaliza ordenação

            return lista_ordenada

    def busca(self):
        valor = input('Digite o codigo que está procurando: ')
        tb = int(input('1)Sequencial - 2)Binaria\nOpção: '))
        cont = 0
        achou = False

        if tb is 1:
            lista = self.apresentarRegistro()
            codigos = []
            resto = []

            for dados in lista:
                armazena = dados.split()
                codigos.append(armazena[0])
                resto.append(armazena[1] + ' do Autor ' + armazena[2])

            for dados2 in codigos:

                if achou is False:
                    cont += 1

                    if valor == dados2:
                        print('\nlivro %s encontrado após a verificação de %s codigos' % (resto[cont - 1], cont))
                        achou = True

            if not achou:
                print('livro não encontrado')

        elif tb is 2:
            lista_ordenada = self.ordenar()
            codigos = []
            resto = []

            for dados in lista_ordenada:
                armazena = dados.split()
                codigos.append(armazena[0])
                resto.append(armazena[1] + ' do Autor ' + armazena[2])

            esqd = 0
            dirt = len(codigos) - 1

            while esqd <= dirt:
                cont += 1
                meio = (esqd + dirt) // 2

                if valor == codigos[meio]:
                    print('\nlivro %s encontrado após a verificação de %s codigos' % (resto[meio], cont))
                    achou = True
                    break

                elif codigos[meio] > valor:
                    dirt = meio - 1

                else:
                    esqd = meio + 1

            if not achou:
                print('livro não encontrado')

        else:
            print('Codigo invalido')


d = Livro()
d.criarArquivo()
while True:
    try:
        op = int(input('\n1)Cadastrar livro\n2)Apresentar Registro\n3)Realizar busca\n4)Sair\nOpção: '))

        if op is 1:
            c = input('\nDigite o codigo do livro(apenas numeros): ')
            if not c.isdigit():  # Caso os codigos sejam só atraves de numeros
                print('O codigo precisa ser um numero.')
                continue
            t = input('\nDigite o titulo do livro:  ')
            a = input('\nDigite o nome do autor: ')
            d.cadastrarLivro(c, t, a)

        elif op is 2:
            print('REGISTRO\nCODIGO|TITULO|AUTOR\n')

            if d.apresentarRegistro() != 'Registro vazio':
                for dados_arquivo in d.apresentarRegistro():
                    print(dados_arquivo)

            else:
                print(d.apresentarRegistro())

        elif op is 3:
            d.busca()

        elif op is 4:
            print('Programa encerado.')
            break
        else:
            print('Opção invalida')

    except ValueError as error:
        print('Erro - Você deve digitar valores inteiros: %s' % error)
    except Exception as ex:
        print('Erro inesperado: %s' % ex)
