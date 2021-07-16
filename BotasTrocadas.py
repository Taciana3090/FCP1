class Nodo():
  def __init__(self, data=None):
    self._data = data
    self._sucessor = None
    self._antecessor = None

  def __str__(self):
    return str(self._data)

class Lista():
  def __init__(self):
    self._comeco = None
    self._final = None

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

  def inserirNoFim(self, data=None):
    novo_nodo = Nodo(data)
    if self.isVazia() == True:
      self._comeco = self._final = novo_nodo
    else:
      novo_nodo._antecessor = self._final
      self._final._sucessor = novo_nodo
      self._final = novo_nodo

  def isVazia(self):
    return self._comeco is None and self._final is None

  def buscar(self,x):
    i = self._comeco
    while not i == None:
      if x == i._data:
        break
        i = i._sucessor
    return i

  def removerElemento(self,x):
    nodo_encontrado = self.buscar(x)
    if nodo_encontrado != None:
      if nodo_encontrado._antecessor != None:
        nodo_encontrado._antecessor._sucessor = nodo_encontrado._sucessor
      else:
        self._começo = nodo_encontrado._sucessor
      if nodo_encontrado._sucessor != None:
        nodo_encontrado._sucessor._antecessor = nodo_encontrado._antecessor
      else:
        self._final = nodo_encontrado._antecessor
    return nodo_encontrado

  def quantidade(self,x):
    cont = 0
    i = self._comeco
    while not i is None:
      if x == i._data:
        cont +=1
      i = i._sucessor
    return cont

BotaDireita = Lista()
BotaEsquerda = Lista()
N = int(input())
for i in range(N):
  valores = input()
  partes = valores.split()
  M = int(partes[0])
  L = str(partes[1])
  if L == 'D':
    BotaDireita.inserirNoFim(int(M))
  if L == 'E':
    BotaEsquerda.inserirNoFim(int(M))

PeEsquerdo = 0
PeDireito = 0
Pares = 0
for i in range(30, 60+1):
  PeEsquerdo += BotaEsquerda.quantidade(i)
  PeDireito += BotaDireita.quantidade(i)
  Pares += min(PeEsquerdo,PeDireito)
  PeDireito = PeEsquerdo = 0
print(Pares)