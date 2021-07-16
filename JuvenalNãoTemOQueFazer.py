# Conta g recursivo
def g(intervalo,contagem=0):
    contagem += 1
    #Se todos os números no intervalo forem igual a 1 acaba e retorna a contagem.
    if intervalo.count(1) == len(intervalo):
        return contagem
#Para g diferente de 1, aplica a função g em cada numero do intervalo.
    for i in range(len(intervalo)):
        if intervalo[i] !=1:
            if intervalo[i] % 2 == 0:
                intervalo[i] = intervalo[i]//2
            else:
                intervalo[i] = 3*intervalo[i]+1
    #Chama g recursivamente para o novo intervalo.
    return g(intervalo,contagem)


##################################
# PROGRAMA PRINCIPAL
#################################
num_casos = int(input())
entradas = []

for i in range(0,num_casos):
    #Lê os limites a e b da entrada padrão e armazena como intervalo na lista entradas
    entradas.append(list(map(int,input().split(" "))))

for i in range (0,num_casos):
    #Imprime o máximo de g naquele intervalo
    print("Caso " + str(i + 1) + ": " + str(g(list(range(entradas[i][0], entradas[i][1] + 1)))))