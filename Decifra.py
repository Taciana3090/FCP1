# Função que separa os caracteres de uma string e retorna uma lista de caracteres
def separa(palavra):
    return [char for char in palavra]
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Lê a chave de encriptacao
chave = input()
# Cria um dicionário contendo as correspondências
crivo = dict(zip(separa(chave),separa(alfabeto)))

# Lê a frase a decriptar
frase = input()

#Inicializa um string vazia
frase_decriptada = ""

#Percorre as letras da frase
for letra in frase:
    #Obtem a letra correspondente do dicionário e concatena na string
    frase_decriptada  += crivo.get(letra)

print(frase_decriptada)
