"""
Comparação experimental de dois algoritmos de distância de edição (edit-distance):
  • edit_distance_memo       – abordagem top-down (recursiva) com memoização
  • edit_distance_bottom_up  – abordagem bottom-up (iterativa)

Conforme o enunciado:
  • 10 ≤ n ≤ 10 000
  • 100 ≤ k ≤ 200   (nº de tamanhos de entrada distintos, igualmente espaçados)
  • 10 ≤ m ≤ 20     (nº de instâncias por tamanho, mesmo para todos os n)
  • As mesmas instâncias são usadas para os dois algoritmos.
"""

import random
import string
import sys
import time
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 1) Algoritmo top-down recursivo com memoização
# ---------------------------------------------------------------------------
def edit_distance_memo(x: str, y: str) -> int:
    m, n = len(x), len(y)
    ed = [[-1] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        ed[i][0] = i
    for j in range(n + 1):
        ed[0][j] = j

    # garante profundidade de pilha suficiente
    sys.setrecursionlimit(max(50_000, 2 * (m + n)))

    def rec(i: int, j: int) -> int:
        if ed[i][j] >= 0:
            return ed[i][j]

        cost = 0 if x[i - 1] == y[j - 1] else 1
        ed[i][j] = min(
            rec(i - 1, j - 1) + cost,  # diagonal (match / substituição)
            rec(i - 1, j) + 1,         # cima     (remoção)
            rec(i, j - 1) + 1          # esquerda (inserção)
        )
        return ed[i][j]

    return rec(m, n)


# ---------------------------------------------------------------------------
# 2) Algoritmo bottom-up iterativo
# ---------------------------------------------------------------------------
def edit_distance_bottom_up(x: str, y: str) -> int:
    m, n = len(x), len(y)
    ed = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        ed[i][0] = i
    for j in range(n + 1):
        ed[0][j] = j

    for i in range(1, m + 1):
        xi = x[i - 1]
        row_i   = ed[i]
        row_prev = ed[i - 1]
        for j in range(1, n + 1):
            cost = 0 if xi == y[j - 1] else 1
            diag = row_prev[j - 1] + cost
            up   = row_prev[j] + 1
            left = row_i[j - 1] + 1
            row_i[j] = diag if diag <= up and diag <= left else (left if left <= up else up)

    return ed[m][n]


# ---------------------------------------------------------------------------
# 3) Parâmetros exatamente como no enunciado
# ---------------------------------------------------------------------------
MIN_N, MAX_N = 10, 10_000          # intervalo de tamanhos das strings
K_RANGE      = (100, 200)          # nº de tamanhos distintos
M_RANGE      = (10, 20)            # nº de instâncias por tamanho
ALPHABET     = string.ascii_lowercase


def main() -> None:
    random.seed(42)                # reprodutibilidade

    k = random.randint(*K_RANGE)   # sorteia k
    m = random.randint(*M_RANGE)   # sorteia m  (mesmo para todos os n)

    # tamanhos igualmente espaçados
    step = (MAX_N - MIN_N) / (k - 1)
    sizes = [int(MIN_N + i * step) for i in range(k)]

    time_memo, time_bottom = [], []

    for n in sizes:
        total_memo, total_bottom = 0.0, 0.0

        # gera *uma única* lista de pares (s1, s2) para este n
        instances = [
            (
                ''.join(random.choices(ALPHABET, k=n)),
                ''.join(random.choices(ALPHABET, k=n))
            )
            for _ in range(m)
        ]

        # executa os dois algoritmos sobre as MESMAS instâncias
        for s1, s2 in instances:
            start = time.perf_counter()
            d1 = edit_distance_memo(s1, s2)
            total_memo += time.perf_counter() - start

            start = time.perf_counter()
            d2 = edit_distance_bottom_up(s1, s2)
            total_bottom += time.perf_counter() - start

            # verificação de correção
            assert d1 == d2, f"Distâncias divergentes (n={n})"

        time_memo.append(total_memo / m)
        time_bottom.append(total_bottom / m)
        print(f"n={n:5d}  OK  memo={time_memo[-1]:.3f}s  bottom={time_bottom[-1]:.3f}s")

    # -----------------------------------------------------------------------
    # 4) Plotagem
    # -----------------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, time_memo,   label="Top-down memoização")
    plt.plot(sizes, time_bottom, label="Bottom-up iterativo")
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo médio por instância (s)")
    plt.title(f"Comparação de tempo – k={k}, m={m}")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
