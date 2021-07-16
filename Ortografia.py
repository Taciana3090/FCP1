#Função que calcula a distância mínima com base em programação dinâmica
def min_distancia(p1, p2):
    #Matriz que armazenará o número de operações na transformação das palavras
    tabela = [[0 for a in range(len(p1)+1)] for a in range(len(p2)+1)]
    #Atribui 0 a célula superior do lado esquerdo da tabela, caso não tenha char para realizar transformações.
    tabela[0][0] = 0
    #Na primeira linha da tabela, copia a contagem anterior adicionando 1, pois não tem nada para comparar entre as strings.
    for i in range(1, len(p1)+1):
        tabela[0][i] = tabela[0][i-1] + 1
    #Ao contrário, estando na coluna mais a esquerda tabela, tira-se da célula acima da atual, adicionando 1 na atual
    #sendo assim, não é necessário realizar nenhuma operação na p2, só adiciona o próximo char.
    for i in range(1, len(p2)+1):
        tabela[i][0] = tabela[i-1][0] + 1
    for i in range(1, len(p2)+1):
        for j in range(1, len(p1)+1):
            #Se forem correspondentes (chars), pegará apenas o número de operações da célula diagonal à esquerda (acima da tabela)
            if p2[i - 1] == p1[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1]
            #Senão, pega o mínimo entre a célula diagonal (acima da atual), célula superior ou a esquerda
            else:
                tabela[i][j] = min(tabela[i][j - 1], tabela[i - 1][j], tabela[i - 1][j - 1]) + 1
    return tabela[len(tabela)-1][len(tabela[0])-1]


#############################
# Programa Principal
#############################

n, m = [int(i) for i in input().split()]
dicionario = [0 for x in range(n)]
palavras_erradas = [0 for x in range(m)]
for i in range(n):
    dicionario[i] = input().lower()

for i in range(m):
    palavras_erradas[i] = input().lower()

for palavra in palavras_erradas:
    resultado_palavra = ""
    for palavra_dicionario in dicionario:
        if min_distancia(palavra_dicionario, palavra) < 3:
            resultado_palavra += palavra_dicionario + " "
    print(resultado_palavra[:-1])