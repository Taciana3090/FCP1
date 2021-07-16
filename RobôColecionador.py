orientacoes = [(-1, 0), (0, 1), (1, 0), (0, -1)]
orientacoes_b = ['N', 'L', 'S', 'O']

while(True):

    qtd = 0
    figurinhas = 0

    N, M, S = map(int, input().split())

    if (N, M, S) == (0, 0, 0):
        break
    
    arena = []
    # indice de orientacao
    orientacao = 0
    coordenadas = (0, 0)

    for i in range(0, N):
        
        arena.append("_".join(input()).split("_"))

        for orient in orientacoes_b:
            if orient in arena[i]:
                orientacao = orientacoes_b.index(orient)
                coordenadas = (i, arena[i].index(orient))
                break

    instrucoes = input('')

    for instrucao in instrucoes:

        if instrucao == 'D':
            # indice da orientacao horaria seguinte
            orientacao += 1
            if orientacao == 4:
                orientacao = 0

        if instrucao == 'E':
            # indice da orientacao anti horaria seguinte
            orientacao -= 1
            if orientacao == -1:
                orientacao = 3
        
        if instrucao == 'F':
            #avanca o robo, seguindo a orientacao -> coords (x, y) + orient (a, b) = novas coords (x+a, y+b)
            # novas_coords = tuple(map(lambda x,y: x+y, coordenadas, orientacoes[orientacao]))
            novas_coords = (coordenadas[0] + orientacoes[orientacao][0], coordenadas[1] + orientacoes[orientacao][1])

            #se as coordenadas passaram da linha N ou 0
            if novas_coords[0] >= N or novas_coords[0] < 0:
                continue

            #se as coordenadas passaram da linha M ou 0
            if novas_coords[1] >= M or novas_coords[1] < 0:
                continue

            #se as coordenadas deram em uma pilastra
            if arena[novas_coords[0]][novas_coords[1]] == '#':
                continue

            if arena[novas_coords[0]][novas_coords[1]] == '*': #se a celula da nova coordenada for uma figurinha
                arena[novas_coords[0]][novas_coords[1]] = '.' #retira a figurinha da arena
                figurinhas += 1 #adiciona no somador

            coordenadas = novas_coords #atualiza as coordenadas

    print(figurinhas)