# Operação sucessor
def suc(n):
    return n+1

# Soma usando sucessor
def soma(a, b):
    for i in range(b):
        a = suc(a)

    return a

# Multiplicação usando soma
def mult(a, b):
    m = 0
    for i in range(b):
        m = soma(m, a)

    return m

# Expoente usando multiplicação
def Exp(a, b):
    e = 1
    for i in range(b):
        e = mult(e, a)

    return e

#######################################
#       Programa principal
#######################################



while True:
    # Lê a entrada e separa nos espaços.
    entrada = input().split()


    # Para cada operação faz o cálculo solicitado.
    if entrada[0] == "Suc": # Sucessor
        print(suc(int(entrada[1])))
    elif entrada[0] == "Soma": # Soma
        print(soma(int(entrada[1]),int(entrada[2])))
    elif entrada[0] == "Mult": # Multiplicação
        print(mult(int(entrada[1]),int(entrada[2])))
    elif entrada[0] == "Exp": # Exponenciação
        print(Exp(int(entrada[1]),int(entrada[2])))
    else:
        break
