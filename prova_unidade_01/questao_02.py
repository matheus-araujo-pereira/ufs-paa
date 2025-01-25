"""
Estratégia usada para resolver a questão:
- busca binária:
    - iniciar os indices inicio e fim;
    - calcular o indice meio como media de inicio e fim;
    - verificar se arr[meio] é o max, se nao for, verificamos em qual direcao continuar, direita arr[meio + 1] ajustando o inicio e esquerda arr[meio - 1] ajustando o fim.
"""


def encontrar_maximo(arr):

    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if (meio == 0 or arr[meio] > arr[meio - 1]) and (
            meio == len(arr) - 1 or arr[meio] > arr[meio + 1]
        ):

            return arr[meio]

        elif meio < len(arr) - 1 and arr[meio] < arr[meio + 1]:

            inicio = meio + 1

        else:

            fim = meio - 1

    return -1


exemplo_01 = [10, 8, 3, 2, 1]
exemplo_02 = [1, 4, 5, 7, 8, 9, 20]
exemplo_03 = [0, 2, 5, 7, 13, 9, 8, 7, 2]

print(encontrar_maximo(exemplo_01))
print(encontrar_maximo(exemplo_02))
print(encontrar_maximo(exemplo_03))
