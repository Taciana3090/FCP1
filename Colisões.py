r1_inf_esqX, r1_inf_esqY, r1_sup_dirX, r1_sup_dirY = [int(coordenada) for coordenada in input().split()]
r2_inf_esqX, r2_inf_esqY, r2_sup_dirX, r2_sup_dirY = [int(coordenada) for coordenada in input().split()]

if(r1_sup_dirX < r2_inf_esqX or r1_sup_dirY < r2_inf_esqY or
        r2_sup_dirX < r1_inf_esqX or r2_sup_dirY < r1_inf_esqY):
        print(0)
else:
    print(1)




