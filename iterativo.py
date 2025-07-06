def edit_distance_pd(x, y):
    m, n = len(x), len(y)

    # Criação das matrizes
    ed = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    R = [['' for _ in range(n + 1)] for _ in range(m + 1)]

    # Inicialização da primeira coluna (remoções)
    for i in range(m + 1):
        ed[i][0] = i
        R[i][0] = '↑'

    # Inicialização da primeira linha (inserções)
    for j in range(n + 1):
        ed[0][j] = j
        R[0][j] = '←'

    # Preenchimento das tabelas
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dif = 0 if x[i - 1] == y[j - 1] else 1

            diag = ed[i - 1][j - 1] + dif
            left = ed[i][j - 1] + 1
            up = ed[i - 1][j] + 1

            if diag <= min(left, up):
                ed[i][j] = diag
                R[i][j] = '↘'
            elif left <= up:
                ed[i][j] = left
                R[i][j] = '←'
            else:
                ed[i][j] = up
                R[i][j] = '↑'

    return ed[m][n], R

# Dessa Linha em Diante é um teste Simples
x = "gato"
y = "rato"

distancia, R = edit_distance_pd(x, y)

print(f"Distância de edição: {distancia}")
print("Matriz de reconstrução:")
for linha in R:
    print(' '.join(linha))
