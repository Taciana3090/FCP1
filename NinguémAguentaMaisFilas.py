#nodo de listas duplamente encadedadas
class nodo():
    def __init__(self, data=None):
        self._data = data
        self._sucessor = None
        self._antecessor = None

    def __str__(self):
        return str(self._data)

#list duplamente encadeada
class list():
    def __init__(self):
        self._comeco = None
        self._final = None

    #Gerar a string
    def __str__(self):
        f = ""
        c = self._comeco
        while not c is None:
            if c._sucessor == None:
                f += "{}".format(str(c))

            else:
                f += "{} ".format(str(c))
            c = c._sucessor
        return f

    def coloca_no_final(self, data=None):
        novo_nodo = nodo(data)
        if self.desocupada():
            self._comeco = self._final = novo_nodo

        else:
            novo_nodo._antecessor = self._final
            self._final._sucessor = novo_nodo
            self._final = novo_nodo

    def desocupada(self):
        return self._comeco is None and self._final is None

    def cata(self, x):
        y = self._comeco
        while not y is None:
            if x == y._data:
                break
            else:
                y = y._sucessor
        return y

    def remove(self, x):
        nodo_achado = self.cata(x)
        if nodo_achado is not None:
            if nodo_achado._sucessor is not None:
                nodo_achado._sucessor._antecessor = nodo_achado._antecessor
            else:
                self._final = nodo_achado._antecessor

            if nodo_achado._antecessor is not None:
                nodo_achado._antecessor._sucessor = nodo_achado._sucessor
            else:
                self._comeco = nodo_achado._sucessor

        return nodo_achado



qnt_pessoas_inicialmente = [int(n) for n in input().split()]
ident_pessoa_inicialmente = input().split()
qnt_pessoas_deixaram_fila = [int(m) for m in input().split()]
ident_pessoas_deixaram_fila = input().split()
lista_pessoas = list()
for i in ident_pessoa_inicialmente:
    lista_pessoas.coloca_no_final(i)
for i in ident_pessoas_deixaram_fila:
    lista_pessoas.remove(i)
print(lista_pessoas)