#Função que irá identificar o número diferente na lista
def identifica_diferente(lista):
#Transforma lista em conjunto e depois em lista novamente, para obter apenas os valores únicos da lista
    valores_unicos = list(set(lista))
#Percorre cada valor único
    for valor in valores_unicos:
    #Irá contar quantas vezes o valor único aparece na lista
        contagem = 0
        for num in lista:
           #Se o número na lista for igual ao valor único
            if num == valor:
            #Então adicionou à contagem
                contagem += 1
            #Se já contou o valor mais de uma vez, então ele não é único
            if contagem > 1:
            #Então quebra-se o laço
                break
        #Se após rodar a lista inteira, só contamos aquele valor uma única vez
        if contagem == 1:
        #Então o valor único foi encontrado, e quebra-se o laço
            break
#Retornará a posição na lista onde o valor único se encontra
    return lista.index(valor)

######################

# Programa principal

######################
# Lê as dimensões
n = int(input())
quadrado = []
#Lê cada linha do quadrado
for i in range(n):

    quadrado.append(list(map(int, input().split(" "))))

# Inicializa soma das linhas com a das colunas
soma_linhas = []
soma_colunas = [0]*n
#Para cada linha do quadrado
for linha in quadrado:
    #Soma os valores da linha e adiciona à lista soma_linhas
    soma_linhas.append(sum(linha))

    #Para cada elemento da linha
    for i in range(n):
        #Soma no elemento correspondente da lista soma_colunas
        soma_colunas[i] += linha[i]
#Identifica o elemento diferente na linha e na coluna, obtendo suas coordenadas
linha_diferente = identifica_diferente(soma_linhas)
coluna_diferente = identifica_diferente(soma_colunas)
#Então encontra o número diferente pelas coordenadas
numero_diferente = quadrado[linha_diferente][coluna_diferente]

#Apenas uma linha está errada, então a linha 0 ou 1 vai estar correta
#Se a linha 0 estiver correta(sua soma é diferente da soma da linha diferente)
if soma_linhas[0] != soma_linhas[linha_diferente]:
    #Então o número certo pode ser calculcado
    numero_certo = numero_diferente - soma_linhas[linha_diferente] + soma_linhas[0]
#Se a linha 0 for a linha com número diferente, então a linha 1 possui a soma certa
else:
    #Então calculamos o número certo com a linha 1
    numero_certo = numero_diferente - soma_linhas[linha_diferente] + soma_linhas[1]
#Imprimirá o número correto e o número diferente
print(numero_certo, numero_diferente)