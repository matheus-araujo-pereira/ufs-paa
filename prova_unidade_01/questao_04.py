"""
Estratégia usada para resolver a questão:
- ordenar os pontos pela coordenada X;
- comecar com os 2 pontos mais extremos PE e PD;
- iterar e avaliar a curvatura dos pontos seguintes para construir o poligono convexo;
- se um ponto formar uma curva à direita, removemos o ponto do conjunto.
"""

def produto_vetorial(p1, p2, p3):

    termo_1 = p2[0] - p1[0]
    termo_2 = p3[1] - p2[1]
    termo_3 = p2[1] - p1[1]
    termo_4 = p3[0] - p2[0]

    return termo_1 * termo_2 - termo_3 * termo_4

def envoltorio_convexo(S):

    S = sorted(S)

    inferior = []
    superior = []

    for p in S:

        while len(inferior) >= 2 and produto_vetorial(inferior[-2], inferior[-1], p) <= 0:

            inferior.pop()

        inferior.append(p)
    
    for p in reversed(S):

        while len(superior) >= 2 and produto_vetorial(superior[-2], superior[-1], p) <= 0:

            superior.pop()

        superior.append(p)

    del inferior[-1]
    del superior[-1]

    envoltorio = inferior + superior

    return envoltorio

exemplo_01 = [(0, 0), (1, 1), (2, 0)]
exemplo_02 = [(0, 0), (0.9, 0.1), (1, 1), (2, 0), (1, -1)]

print("Envoltório convexo para o exemplo_01:", envoltorio_convexo(exemplo_01))
print("Envoltório convexo para o exemplo_02:", envoltorio_convexo(exemplo_02))