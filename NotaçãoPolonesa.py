class No():
    def __init__(self, dado=None):
        self.prox_ = None
        self.dado_ = dado

class Pilha():
    def __init__(self):
        self.inicio_ = None

    def empilhar(self, dado):
        novono = No(dado)
        novono.prox_ = self.inicio_
        self.inicio_ = novono

    def isVazia(self):
        return self.inicio_ is None

    def desempilhar(self):
        if not self.isVazia():
            saida = self.inicio_
            self.inicio_ = self.inicio_.prox_
            return saida.dado_
        return None



while True:
    linha_de_entrada = input()
    if linha_de_entrada:
        lista_de_operacoes = linha_de_entrada.split()
        pilha = Pilha()
        for i in range(len(lista_de_operacoes)-1, -1, -1):
            if lista_de_operacoes[i] == "+":
                operando1 = pilha.desempilhar()
                operando2 = pilha.desempilhar()
                resultado = operando1 + operando2
                pilha.empilhar(resultado)
            elif lista_de_operacoes[i] == "-":
                operando1 = pilha.desempilhar()
                operando2 = pilha.desempilhar()
                resultado = operando1 - operando2
                pilha.empilhar(resultado)
            elif lista_de_operacoes[i] == "*":
                operando1 = pilha.desempilhar()
                operando2 = pilha.desempilhar()
                resultado = operando1 * operando2
                pilha.empilhar(resultado)
            elif lista_de_operacoes[i] == "/":
                operando1 = pilha.desempilhar()
                operando2 = pilha.desempilhar()
                resultado = int(operando1 / operando2)
                pilha.empilhar(resultado)
            else:
                pilha.empilhar(int(lista_de_operacoes[i]))
        print(pilha.desempilhar())
    else:
        break
