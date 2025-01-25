"""
Estratégia usada para resolver a questão:
- percorrer o vetor A para encontrar ciclos;
- manter um array para marcar as salas que já foram visitadas;
- coletar as salas envolvidas e manter o maior ciclo encontrado.
"""


def encontrar_ciclos(A):

    N = len(A)
    visitado = [False] * N
    ciclos = []

    def detectar_ciclo(inicio):

        ciclo = []
        atual = inicio

        while not visitado[atual]:

            visitado[atual] = True

            ciclo.append(atual)

            atual = A[atual]

        return ciclo

    for i in range(N):

        if not visitado[i]:

            ciclo = detectar_ciclo(i)

            if ciclo:
                ciclos.append(ciclo)

    maior_ciclo = max(ciclos, key=len) if ciclos else []

    return sorted(maior_ciclo)


exemplo_01 = [3, 3, 3, 0]
exemplo_02 = [1, 2, 3, 4, 0, 7, 5, 1]

print(encontrar_ciclos(exemplo_01))
print(encontrar_ciclos(exemplo_02))
