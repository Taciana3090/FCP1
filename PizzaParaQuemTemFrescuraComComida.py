#inicializa com zeros
fatia = [0 for _ in range(100000)]
melhor_soma = [0 for _ in range(100005)]
soma = [0 for _ in range(100005)]

#Função que calcula o máximo
def calcula_maximo(x, y):
    if x > y:
        return x
    return y

#Lê as entradas
n = int(input())
if n != 0:
    fatia = [int(c) for c in input().split()]
#Verifica se a entrada foi bem formada, se não for acrescenta zeros até ela ser
if len(fatia) < n:
    tamanho_atual = len(fatia)
    for i in range(n - tamanho_atual):
        fatia.append(0)
for i in range(n):
    #Calcula o saldo de cebolas da fatia 0 até a i-1
    soma[i + 1] = soma[i] + fatia[i]
    #Guarda o melhor resultado encontrado até a fatia i
    melhor_soma[i + 1] = calcula_maximo(melhor_soma[i], soma[i + 1])
valor_maximo = 0


for i in range(n + 1):
    #Guarda o valor máximo considerando que podemos conectar o comeco com o fim
    valor_maximo = calcula_maximo(valor_maximo, melhor_soma[i] + (soma[n] - soma[i]))
    #veja que soma[n]-soma[i] é a soma do saldo das "n-i" ultimas fatias

    #Agora tem que ver se existe alguma sequencia de fatias intermediarias, de tal forma que seu saldo
    #seja melhor que o melhor saldo que já foi calculado anteriormente
fatias_intermediarias = 0

for i in range(n):
    #se em algum momento chegar em um saldo menor do que zero, é melhor "zerar" a contagem e comecar a contar novamente
    fatias_intermediarias = calcula_maximo(0, fatias_intermediarias + fatia[i])
    valor_maximo = calcula_maximo(valor_maximo, fatias_intermediarias)

print(valor_maximo)
