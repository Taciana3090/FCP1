# Lê N da entrada padrão
n = int(input())
# Lê a sequência de números e armazena em lista
lista = list(map(int,input().split(" ")))
# Calcula a soma de todos os números entre 1 e 10
total = n *(n+1)//2
# O número que falta é a diferença entre a soma dos números da lista e o total.
print(total-sum(lista))