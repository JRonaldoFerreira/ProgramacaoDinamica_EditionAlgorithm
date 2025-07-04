# Comparação Empírica de Abordagens Top-Down e Bottom-Up para a Distância de Edição
### José Ronaldo Ferreira Braga da Silva Filho¹ · Raul Santiago Pinheiro¹  
¹Graduação em Ciência da Computação – Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE), Campus Maracanaú – Brasil  
{ jose.ronaldo.ferreira07@aluno.ifce.edu.br · raul.santiago.pinheiro00@aluno.ifce.edu.br }

---

## Abstract  
The edit-distance (or Levenshtein distance) measures the minimum number of elementary operations (insertion, removal, and substitution) required to transform one string into another.  
This work empirically compares two classical implementations of the algorithm: (i) a recursive top-down version with memoisation and (ii) an iterative bottom-up version.  
Up to 5 000 artificial instances of sizes \(10 \le n \le 5\,000\) were generated, with 100–200 distinct sizes and 10–20 instances per size.  
Average execution times were measured and cross-checked for correctness.  
Both strategies keep the theoretical \( \mathcal{O}(n^2) \) complexity, but the recursive approach is ~7–9 × slower at \( n = 5\,000 \). Causes––recursive-call overhead, cache effects, and stack management––are discussed and optimisation paths are proposed. :contentReference[oaicite:0]{index=0}  

## Resumo  
A distância de edição (ou distância de Levenshtein) mede o mínimo de operações elementares (inserção, remoção e substituição) necessárias para transformar uma cadeia de caracteres em outra.  
Compara-se empiricamente: (i) uma versão top-down recursiva com memoização e (ii) uma versão bottom-up iterativa.  
Geraram-se até 5 000 instâncias artificiais com \(10 \le n \le 5\,000\), 100–200 tamanhos distintos e 10–20 instâncias por tamanho.  
Os tempos médios foram medidos e verificados para correção. Confirmou-se \( \mathcal{O}(n^2) \) em ambas, mas o método recursivo apresenta fator ~7–9 × de sobrecarga quando \( n = 5\,000 \). Discutem-se sobrecarga de chamadas recursivas, fragmentação de cache e gestão de pilha, e apontam-se otimizações futuras. :contentReference[oaicite:1]{index=1}  

**Palavras-chave / Keywords:** edit distance · programming dynamics · memoisation · experimental evaluation · algorithmic complexity  

---

## 1. Introdução
A distância de Levenshtein é amplamente empregada em bioinformática, correção ortográfica e recuperação de informação. Embora existam variantes sub-quadráticas para casos específicos, a formulação clássica permanece relevante em aplicações onde a simplicidade se sobrepõe ao desempenho extremo. Duas abordagens dominam:

* **Top-down com memoização** – define-se a recorrência e armazena-se cada subproblema resolvido.  
* **Bottom-up iterativa** – preenche-se explicitamente a tabela dinâmica a partir dos casos-base.  

Na teoria, ambas requerem \( \Theta(nm) \) em tempo e memória, mas a sobrecarga prática difere; este artigo quantifica tal diferença.

## 2. Metodologia

### 2.1 Algoritmos  
As Listagens 1 e 2 (vide */src/*) trazem as implementações Python.  
A versão top-down ajusta a profundidade de pilha via `sys.setrecursionlimit`; a iterativa reutiliza linhas da matriz para melhor localidade de cache.

### 2.2 Geração dos dados  

| Parâmetro | Faixa | Observação |
|-----------|-------|-----------|
| Alfabeto  | `a`–`z` |
| Tamanhos \(n\) | 100–200 valores em \([10, 5 000]\) | igualmente espaçados |
| Instâncias por \(n\) | 10–20 | mesmo valor para todos os \(n\) |
| Semente | `random.seed(42)` | reprodutibilidade |

### 2.3 Procedimento  
1. Para cada \(n\), gerar \(m\) pares de cadeias aleatórias.  
2. Executar **ambos** os algoritmos sobre os mesmos pares.  
3. Medir o tempo via `time.perf_counter()`.  
4. Verificar \(d_\text{memo} = d_\text{bottom}\) com `assert`.

### 2.4 Ambiente de teste  
* Intel i7-11700 (8 c/16 t · 2.5–4.9 GHz)  
* 32 GB DDR4-3200  
* Python 3.12 · matplotlib 3.9  
* Ubuntu 24.04 LTS  

## 3. Resultados  

![Figura 1 — Tempo médio por instância](./figures/fig1_tempo_medio.png)

> **Figura 1.** Tempo médio por instância dos algoritmos top-down e bottom-up (k = 181, m = 11).

### 3.1 Tabela-amostra  

| \(n\) | Bottom-up (s) | Top-down (s) | Fator |
|------:|--------------:|-------------:|------:|
| 10    | 0.00013 | 0.00019 | 1.5× |
| 1 000 | 0.47    | 3.20    | 6.8× |
| 2 500 | 2.10    | 17.9    | 8.5× |
| 5 000 | 7.40    | 65.7    | 8.9× |

## 4. Discussão  

1. **Sobrecarga de chamadas recursivas** – empilhamento/desempilhamento custa caro.  
2. **Localidade de cache** – acesso sequencial da versão iterativa favorece caching; a recursiva faz saltos.  
3. **Gestão de pilha** – necessidade de `recursionlimit` elevado acarreta reservas de memória adicionais.  
4. **Estouro de pilha** – limitações de ambiente podem inviabilizar a solução recursiva.

## 5. Conclusão e Trabalhos Futuros  
* A equivalência funcional foi confirmada; a estratégia bottom-up mostrou-se até **9×** mais veloz para \( n = 5 000 \).  
* Futuras linhas de pesquisa: otimizações de espaço (duas linhas), algoritmos sub-quadráticos (Myers), testes com alfabetos maiores, paralelização GPU/SIMD.

---

## Referências  

1. Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. *Introduction to Algorithms*, 3 ed. MIT Press, 2009.  
2. Levenshtein, V. I. Binary codes capable of correcting deletions, insertions and reversals. *Soviet Physics Doklady*, 10 (8): 707-710, 1966.  
3. Wagner, R. A.; Fischer, M. J. The string-to-string correction problem. *Journal of the ACM*, 21 (1): 168-173, 1974.  
4. Myers, G. A. A fast bit-vector algorithm for approximate string matching based on dynamic programming. *JACM*, 46 (3): 395-415, 1999.  

---

> *Para inserir o PDF completo ou mais figuras, crie uma pasta `/docs` ou `/figures` e referencie-as com os caminhos relativos adequados.*  
> *Qualquer ajuste de formatação (ABNT, IEEE, etc.) ou inclusão de mais seções pode ser solicitado.*  
