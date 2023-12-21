%% *****************************************************************************

:- dynamic
    %% Questão 01: definir a base de conhecimentos
    futebol/5.
    %% Questão 02: definir o fato maior equipe
    maior/2.

%% *****************************************************************************

load_futebol(FileName):-
    %% Questão 03: Criar a regra que carrega a base de conhecimentos
    exists_file(FileName),
    write('Consultando [Futebol.bas.txt]...'),
    consult(FileName),
    write('Ok.'),nl,
    write('Equipes de futebol:'),nl,
    print_futebol,
    inicia_busca,
    fim_busca,!.

%% *****************************************************************************

print_futebol:-
    %% Questão 04: Criar a regra que imprime todas as equipes de futebol
    %%             Use quatro espaços para separar os atributos de cada equipe
    futebol(Nome, Titulos, Estado, Cidade, Cores),
    write('Nome: '),
    write(Nome),
    write('    Títulos: '),
    write(Titulos),
    write('    Estado: '),
    write(Estado),
    write('    Cidade: '),
    write(Cidade),
    write('    Cores: '),
    write(Cores),nl,
    fail.
print_futebol.

%% *****************************************************************************

inicia_busca:-
    assert(maior(nenhum, 0)),
    resultado_busca,
    fail.
    %% Questão 05: Criar a regra que inicia a busca na base de conhecimentos
inicia_busca.

%% *****************************************************************************

resultado_busca:-
    futebol(Nome, Titulos, _Estado, _Cidade, _Cores),
    maior(Eqp, Num),
    (Titulos > Num,
        retract(maior(Eqp, Num)),
        assert(maior(Nome, Titulos))
    ).
    %% Questão 06: Criar a regra que identifica a equipe com mais títulos brasileiros
resultado_busca.

fim_busca:-
    maior(Eqp, Num),
    write('Resultado da busca:'),nl,
    write('Equipe com maior número de títulos: '),
    write(Eqp),nl,
    write('Numero de títulos: '),
    write(Num),nl,
    fail.
fim_busca.
    %% Questão 07: Criar a regra que imprime a equipe com mais títulos brasileiros

%% *****************************************************************************

goal:-
    %% Questão 08: Criar a regra principal do programa
    working_directory(Path, Path),
    string_to_atom('Futebol.bas.txt', Name),
    atom_concat(Path, Name, FileName),
    %% write('FileName: '+FileName),nl,
    load_futebol(FileName).

%% *****************************************************************************
