;; *****************************************************************************

(defglobal ?*filename* = "./Futebol.bas.txt")

(deftemplate futebol
    (slot nome)
    (slot titulos)
    (slot estado)
    (slot cidade)
    (slot cores)
)

;; *****************************************************************************


(deffunction pergunta (?perg)
    (printout t crlf ?perg)
    (bind ?resp (read))
    (return ?resp)
)

;; *****************************************************************************

(defrule load_futebol
    (not (futebol (nome ?)))
    =>
    (printout t "Consultando o arquivo [" ?*filename* "]..." crlf)
    (load-facts ?*filename*)
    (assert (fatos_carregados))
)

;; *****************************************************************************

(defrule print_futebol
    (fatos_carregados)
    (futebol (nome ?nm) (titulos ?tt) (estado ?es) (cidade ?cd) (cores ?cr))
    =>
    (printout t "nome=" ?nm "    títulos=" ?tt "    estado=" ?es "    cidade=" ?cd "    cores=" ?cr crlf)  
)

;; *****************************************************************************

(defrule inicia_busca
    (fatos_carregados)
    =>
    (assert (maior "nenhuma" 0))
)

;; *****************************************************************************

(defrule resultado_busca
    (fatos_carregados)
    ?pto <- (maior ?eqp ?num)
    (futebol (nome ?nm) (titulos ?tt) (estado ?es) (cidade ?cd) (cores ?cr))
    =>
    (if (< ?num ?tt) then
        (retract ?pto)
        (assert (maior ?nm ?tt)))
)

;; *****************************************************************************

(defrule fim_busca
    (fatos_carregados)
    ?pto <- (maior ?eqp ?num)
    =>
    (retract ?pto)
    (printout t "Resultado da busca:" crlf)
    (printout t "Equipe com maior número de títulos=" ?eqp crlf)
    (printout t "Número de títulos=" ?num crlf)
)

;; *****************************************************************************
