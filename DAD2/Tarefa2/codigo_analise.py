import random
import bisect

class _No_arvoreB(object):
    def __init__(self, valores=None, filhos=None):
        self.pai = None
        self.valores = valores or []
        self.filhos = filhos
        if self.filhos:
            for i in self.filhos:
                i.pai = self

    def __str__(self):
        return 'No\' %r (%d filhos)' % ( self.valores , len(self.filhos) if self.filhos else 0 )

    def imprime(self, tab=''):
        print('%s%s' % (tab, self))
        if self.filhos:
            for i in self.filhos:
                i.imprime(tab + '   ')

    def check_valid(self, arvore): # checa integridade da arvore
        no_interno = self.filhos is not None
        raiz = self.pai is None
        assert(self.valores is not None)
        # um noh interno(com excessao da raiz) tem, ao menos, min_valores
        if not raiz and no_interno:
            assert(arvore.min_valores <= len(self.valores))
        # um noh nao pode ter mais de max_valores
        assert(len(self.valores) <= arvore.max_valores)
        # a raiz tem, ao menos, dois filhos se nao for uma folha.
        if raiz and no_interno:
            assert(len(self.filhos) >= 2)
        # Um noh que nao seja uma folha com k filhos contem k-1 chaves.
        if no_interno:
            assert((len(self.valores) + 1) == len(self.filhos))
        # checa se os valores estao ordenados
        prev = None
        for i in self.valores:
            if prev is not None:
                assert(i > prev)
            prev = i
        if self.filhos:
            for i in self.filhos:
                assert(i.pai is self)
                i.check_valid(arvore)

    def buscar(self, valor):
        '''
        retorna um registro. Se o valor existir (True, noh, posicao),
        caso contrario (False, noh, posicao onde deveria ser inserido)
        '''
        i = bisect.bisect_left(self.valores, valor)
        if (i != len(self.valores) and not valor < self.valores[i]):
            # o valor foi encontrado
            assert(self.valores[i] == valor)
            return (True, self, i)

        if self.filhos is not None:
            assert(len(self.filhos) >= i and self.filhos[i])
            # busca recursivamente o noh filhos apropriado
            return self.filhos[i].buscar(valor)
        else:
            return (False, self, i)

    def _split_node(self, arvore, valor=None, slot=None, no_filhos=None):
        '''
        quebra uma arvore B em duas. Se valor for fornecido, insere-o nos nohs resultantes.
        '''
        assert(valor is None or (slot is not None))
        meio_lista = [] if valor is None else [ valor ]
        if slot is None:
            slot = 0
        # pega a media de self.valores e val
        divide_valores = self.valores[0:slot] + meio_lista + self.valores[slot:]
        medianIdx = len(divide_valores) // 2
        valor_esquerdo = divide_valores[0:medianIdx]
        medianVal = divide_valores[medianIdx]
        valor_direito = divide_valores[medianIdx + 1:]
        no_interno = self.filhos is not None
        if no_interno:
            if no_filhos is not None:
                splitfilhos = (self.filhos[0:slot] +
                                 list(no_filhos) +
                                 self.filhos[slot + 1:])
            else:
                splitfilhos = self.filhos
            lc = splitfilhos[0:len(valor_esquerdo) + 1]
            rc = splitfilhos[len(valor_esquerdo) + 1:]
        else:
            lc = None
            rc = None

        no_esquerdo = _No_arvoreB(valor_esquerdo, lc)
        no_direito = _No_arvoreB(valor_direito, rc)
        if self.pai:
            self.pai.add(arvore,
                            medianVal,
                            None,
                            (no_esquerdo, no_direito))
        else:
            # cria nova raiz e incrementa a profundidade da arvore
            newRoot = _No_arvoreB([ medianVal ], [no_esquerdo, no_direito])
            no_esquerdo.pai = newRoot
            no_direito.pai = newRoot
            arvore.root = newRoot
            arvore.height += 1
            arvore.size += 1

    def add(self, arvore, val, slot=None, no_filhos=None):
        '''
        adiciona um novo valor na arvore. o valor nao pode existir previamente
        '''
        assert(self.filhos is None or no_filhos)
        no_interno = self.filhos is not None
        if no_interno:
            assert(no_filhos and len(no_filhos) == 2)
        else:
            assert(no_filhos is None)

        if slot is None:
            slot = bisect.bisect_left(self.valores, val)

        if len(self.valores) < arvore.max_valores:
            self.valores.insert(slot, val)
            arvore.size += 1
            if no_filhos:
                for i in no_filhos:
                    i.pai = self
                self.filhos[slot:slot + 1] = no_filhos
            return True
        self._split_node(arvore, val, slot, no_filhos)
        return True


    def min_value(self, slot=0):
        if self.filhos:
            return self.filhos[slot].min_value()
        return self.valores[0], self, 0

    def max_value(self, slot=None):
        if slot is None:
            slot = len(self.valores) - 1
        if self.filhos:
            return self.filhos[slot + 1].max_value()
        return self.valores[-1], self, len(self.valores) - 1


    def delete(self, arvore, valor, slot=None):
        '''
        remove um valor da arvore. o valor tem de existir previamente
        '''
        no_interno = self.filhos is not None
        if slot is None:
            assert(slot is not None)
            slot = bisect.bisect_left(self.valores, valor)
        assert(slot != len(self.valores) and self.valores[slot] == valor)
        if not no_interno:
            del self.valores[slot]
            arvore.size -= 1
            if len(self.valores) < arvore.min_valores:
                self._rebalance(arvore)
        else:
            novo_sep, no, idx = self.min_value(slot + 1)
            self.valores[slot] = novo_sep
            del no.valores[idx]
            arvore.size -= 1
            if len(no.valores) < arvore.min_valores:
                no._rebalance(arvore)

    def _rebalance(self, arvore):
        '''
        reorganiza a arvore comecando no noh atual
        '''
        lsibling, rsibling, idx = self.get_siblings()
        assert(rsibling or lsibling or self.pai is None)
        if self.pai is None:
            return
        no_interno = self.filhos is not None
        if no_interno:
            assert(rsibling is None or rsibling.filhos is not None)
            assert(lsibling is None or lsibling.filhos is not None)
        else:
            assert(rsibling is None or rsibling.filhos is None)
            assert(lsibling is None or lsibling.filhos is None)
        if not no_interno:
            if rsibling and len(rsibling.valores) > arvore.min_valores:
                sepIdx = idx
                sepVal = self.pai.valores[sepIdx]
                self.pai.valores[sepIdx] = rsibling.valores[0]
                del rsibling.valores[0]
                self.valores.append(sepVal)
                return
            elif lsibling and len(lsibling.valores) > arvore.min_valores:
                sepIdx = idx - 1
                sepVal = self.pai.valores[sepIdx]
                self.pai.valores[sepIdx] = lsibling.valores[-1]
                del lsibling.valores[-1]
                self.valores.insert(0, sepVal)
                return

        if lsibling is not None:
            sepIdx = idx - 1
            ln = lsibling
            rn = self
        elif rsibling is not None:
            sepIdx = idx
            ln = self
            rn = rsibling
        else:
            assert(False)

        sepVal = self.pai.valores[sepIdx]

        ln.valores.append(sepVal)
        ln.valores.extend(rn.valores)
        del rn.valores[:]
        del self.pai.valores[sepIdx]
        assert(self.pai.filhos[sepIdx + 1] is rn)
        del self.pai.filhos[sepIdx + 1]
        if rn.filhos:
            ln.filhos.extend(rn.filhos)
            for i in rn.filhos:
                i.pai = ln

        if len(ln.valores) > arvore.max_valores:
            # we have to split the newly formed node
            # this situation can aris only when merging inner nodes
            assert(no_interno)
            ln._split_node(arvore)

        if len(self.pai.valores) < arvore.min_valores:
            # rebalance the pai
            self.pai._rebalance(arvore)

        if self.pai.pai is None and not self.pai.valores:
            arvore.root = ln
            arvore.root.pai = None

    def get_siblings(self):
        if not self.pai:
            # a raiz nao tem irmaos
            return (None, None, 0)
        assert(self.pai.filhos)
        lsibling = None
        rsibling = None
        idx = 0
        for i, j in enumerate(self.pai.filhos):
            if j is self:
                if i != 0:
                    lsibling = self.pai.filhos[i - 1]
                if (i + 1) < len(self.pai.filhos):
                    rsibling = self.pai.filhos[i + 1]
                idx = i
                break
        return (lsibling, rsibling, idx)

class Barvore(object):
    '''
    cria uma arvore b de ordem 'order'(numero maximo de filhoss por no'),
    que e' o numero maximo de chaves por no' + 1. Retirado de
    The Art of Computer Programming, Knuth, Volume 3 p. 483.
    '''
    def __init__(self, order):
        if order <= 2:
            raise ValueError("a ordem da arvore b deve ser, ao menos, 3")
        self.root = _No_arvoreB()
        self.order = order
        self.max_valores = order - 1
        self.min_valores = self.max_valores // 2
        self.height = 1
        self.size = 0

    def __str__(self):
        return 'altura: %d itens: %d m: %d raiz: %x' % (
                                    self.height, self.size,
                                    self.max_valores + 1,
                                    id(self.root))

    def add(self, val):
        # encontra a folha onde o valor tem de ser inserido
        found, node, slot = self.root.buscar(val)
        if found:
            # o valor ja existe, nao faz nada
            return False
        return node.add(self, val, slot, None)

    def delete(self, val):
        # encontra o valor
        found, node, slot = self.root.buscar(val)
        if not found:
            # o valor nao existe, nao faz nada
            return False
        return node.delete(self, val, slot)

    def buscar(self, val):
        return self.root.buscar(val)[0]

    def min(self):
        return self.root.min_value()[0]

    def max(self):
        return self.root.max_value()[0]


if __name__ == '__main__':
    # mini teste
    obj_arvore = Barvore(3)
    for i in range(20):
        obj_arvore.add(random.randint(0,1000))
        #assert(arvore.buscar(i))
    #for i in range(1, 8):
    #    assert(arvore.buscar(i))

    print("arvore-b")
    obj_arvore.root.imprime()
    print("\n-*o* - - - - - - - - - - - - - - - - *o*-")
    obj_arvore.root.check_valid(obj_arvore)

    for i in range(1, 8):
        obj_arvore.delete(i)
        obj_arvore.root.check_valid(obj_arvore)