def maximo(a,b):

  if a > b:
    return a
  else:
    return b


def tv(n, c, kgs, itens):
    n += 1
    c += 1
    tabela = [[0 for x in range(c)] for x in range(n)]
    for i in range(0, n):
        for j in range(0, c):
            if i == 0 or j == 0:
                tabela[i][j] = 0
            elif kgs[i - 1] > j:
                tabela[i][j] = tabela[i - 1][j]
            elif kgs[i - 1] <= j:
                tabela[i][j] = maximo(itens[i - 1] + tabela[i - 1][j - kgs[i - 1]], tabela[i - 1][j])

    return tabela[i][j]

n,c = [int(i) for i in input().split()]
kgs = []
itens = []
for i in range(n):
    k, i = [int(i) for i in input().split()]
    itens.append(i)
    kgs.append(k)
print(tv(n, c, kgs, itens))