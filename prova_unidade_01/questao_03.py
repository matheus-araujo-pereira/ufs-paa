"""
Estratégia usada para resolver a questão:
- algoritmo bottom-up do mergesort:
    - comecar com sub arrays de tamanho 1;
    - fundir para sub arrays de tamanho 2;
    - fundir para sub arrays de tamanho 4;
    - fundir para sub arrays de tamanho 8;
    - array totalmente ordenado.
"""


def merge(arr, esquerda, meio, direita):

    n1 = meio - esquerda + 1
    n2 = direita - meio

    esquerda_arr = arr[esquerda : meio + 1]
    direita_arr = arr[meio + 1 : direita + 1]

    i = 0
    j = 0
    k = esquerda

    while i < n1 and j < n2:

        if esquerda_arr[i] <= direita_arr[j]:

            arr[k] = esquerda_arr[i]

            i += 1

        else:

            arr[k] = direita_arr[j]

            j += 1

        k += 1

    while i < n1:

        arr[k] = esquerda_arr[i]

        i += 1
        k += 1

    while j < n2:

        arr[k] = direita_arr[j]

        j += 1
        k += 1


def merge_sort_bottom_up(arr):

    n = len(arr)
    tamanho = 1

    while tamanho < n:

        for i in range(0, n - tamanho, 2 * tamanho):

            esquerda = i

            meio = min(i + tamanho - 1, n - 1)

            direita = min(i + 2 * tamanho - 1, n - 1)

            merge(arr, esquerda, meio, direita)

        tamanho *= 2


exemplo = [18, 12, 17, 20, 27, 4, 9]

print("Exemplo original:", exemplo)

merge_sort_bottom_up(exemplo)

print("Exemplo ordenado:", exemplo)
