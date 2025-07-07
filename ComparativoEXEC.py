"""
comparacao_edit_distance.py
-------------------------------------------------
Compara tempo das versões:
  • Edit_memoi / Edit_rec  – top-down com memoização
  • edit_distance_pd       – bottom-up iterativo

"""

import random
import string
import time
import matplotlib.pyplot as plt
import sys 
from recursive import Edit_memoi               # 1) importe sys
from interativo import Edit_distance_pd
# Ajuste a profundidade do limite de recursão

sys.setrecursionlimit(20000)


# --------------------------------------------------------------
# Wrappers de Enpacotamento Das Chamadas dos 2 Algoritmos 
# --------------------------------------------------------------
def edit_distance_memo(s1: str, s2: str) -> int:
    """Empacota Edit_memoi() para receber só (s1, s2)."""
    m, n = len(s1), len(s2)
    ed = [[-1] * (n + 1) for _ in range(m + 1)]  #Tabela de memoização para armazenar os resultados parciais do algoritmo recursivo de distância de edição
    return Edit_memoi(s1, s2, m, n, ed)

def edit_distance_bottom_up(s1: str, s2: str) -> int:
    """Empacota edit_distance_pd() para devolver só a distância."""
    dist, _ = Edit_distance_pd(s1, s2) # Como o segundo argumento de retorno de edit_distance_pd() é uma matriz de direções, aqui está retonrando só a distância
    return dist

# --------------------------------------------------------------
# 2) Parâmetros do experimento (fiéis ao enunciado)
# --------------------------------------------------------------
MIN_N, MAX_N = 10, 800          # intervalo de tamanhos das strings
K_RANGE      = (100, 200)          # nº de tamanhos distintos
M_RANGE      = (10, 20)            # nº de instâncias por tamanho
ALPHABET     = string.ascii_lowercase

# --------------------------------------------------------------
# 3) Função principal
# --------------------------------------------------------------
def main() -> None:
    random.seed(42)                # reprodutibilidade

    k = random.randint(*K_RANGE)   # sorteia k
    m = random.randint(*M_RANGE)   # sorteia m  (mesmo para todos os n)

    step = (MAX_N - MIN_N) / (k - 1)     # tamanhos igualmente espaçados
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

    # ----------------------------------------------------------
    # 4) Plotagem
    # ----------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, time_memo,   label="Top-down memoização")
    plt.plot(sizes, time_bottom, label="Bottom-up iterativo")
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo médio por instância (s)")
    plt.title(f"Comparação de tempo – k={k}, m={m}")
    plt.legend()
    plt.tight_layout()
    plt.show()

# --------------------------------------------------------------
if __name__ == "__main__":
    main()
