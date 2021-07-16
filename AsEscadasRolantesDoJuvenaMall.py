# Lê o número de pessoas que usaram a escada.
num_pessoas = int(input())

instantes = []

# Lê os instantes onde a pessoa usou a escada.
for i in range(num_pessoas):
    instantes.append(int(input()))

total = 0

# Adiciona ao tempo total o tempo que a escada ficou funcionando para a pessoa
# i, isto é, o tempo até a pessoa seguinte usar a escada ou até ela parar.
for i in range(num_pessoas - 1):
    if instantes[i+1] - instantes[i] < 10:
        total += instantes[i+1] - instantes[i]
    else:
        total += 10

# Adiciona o tempo da última pessoa que usou a escada.
total += 10

print(total)