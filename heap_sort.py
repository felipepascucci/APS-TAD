import time
import pandas as pd


def carregar_lista_40k(caminho_arquivo_40k):
    df = pd.read_excel(caminho_arquivo_40k)
    lista = df['Lista 40k'].tolist()
    return lista


def carregar_lista_20k(caminho_arquivo_20k):
    df = pd.read_excel(caminho_arquivo_20k)
    lista = df['Lista 20k'].tolist()
    return lista


def carregar_lista_11k(caminho_arquivo_11k):
    df = pd.read_excel(caminho_arquivo_11k)
    lista = df['Lista 11k'].tolist()
    return lista


def carregar_lista_3k(caminho_arquivo_3k):
    df = pd.read_excel(caminho_arquivo_3k)
    lista = df['Lista 3k'].tolist()
    return lista

# O Heap Sort é um algoritmo de ordenação que funciona da seguinte forma:
# 1- Criando um Heap: Transformamos a lista de números em um Max Heap. Isso significa que o maior número estará no topo do heap.
# 2- Extraindo o Maior Elemento: Removemos o maior elemento (a raiz) do heap e o colocamos no final da lista.
# 3- Reconstruindo o Heap: Reorganizamos o heap para que ele continue sendo um Max Heap.
# 4- Repetindo: Repetimos os passos 2 e 3 até que todos os elementos tenham sido removidos do heap.


def heapify(arr, n, i):
    largest = i  # Inicializa o maior como o nó raiz
    left = 2 * i + 1  # Define o índice do filho à esquerda
    right = 2 * i + 2  # Define o índice do filho à direita

    # Verifica se o filho à esquerda existe e é maior que a raiz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verifica se o filho à direita existe e é maior que o maior até agora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior não for a raiz, troca e continua
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca a raiz com o maior filho
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói um max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move a raiz atual para o final
        heapify(arr, i, 0)  # Chama heapify na árvore reduzida

    return arr 



def medir_tempo_ordenacao(arr):
    tempo_inicial = time.time()
    ordenada = heap_sort(arr)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial

    return ordenada, tempo_total


# Forma de uso:
forma_de_ordenacao = 'heap-sort'

caminho_arquivo_40k = "planilhas/lista40k.xlsx"
lista_40k = carregar_lista_40k(caminho_arquivo_40k)
ordenada, tempo_gasto = medir_tempo_ordenacao(lista_40k)
with open(f"tempoexec/{forma_de_ordenacao}/lista40k.txt", "w") as arquivo:
    arquivo.write("Lista com 40 mil elementos:\n")
    arquivo.write(f"Tempo gasto para ordenar: {tempo_gasto:.6f} segundos\n\n")
    arquivo.write(f"Lista ordenada: {ordenada}")

caminho_arquivo_20k = "planilhas/lista20k.xlsx"
lista_20k = carregar_lista_20k(caminho_arquivo_20k)
ordenada, tempo_gasto = medir_tempo_ordenacao(lista_20k)
with open(f"tempoexec/{forma_de_ordenacao}/lista20k.txt", "w") as arquivo:
    arquivo.write("Lista com 20 mil elementos:\n")
    arquivo.write(f"Tempo gasto para ordenar: {tempo_gasto:.6f} segundos\n\n")
    arquivo.write(f"Lista ordenada: {ordenada}")

caminho_arquivo_11k = "planilhas/lista11k.xlsx"
lista_11k = carregar_lista_11k(caminho_arquivo_11k)
ordenada, tempo_gasto = medir_tempo_ordenacao(lista_11k)
with open(f"tempoexec/{forma_de_ordenacao}/lista11k.txt", "w") as arquivo:
    arquivo.write("Lista com 11 mil elementos:\n")
    arquivo.write(f"Tempo gasto para ordenar: {tempo_gasto:.6f} segundos\n\n")
    arquivo.write(f"Lista ordenada: {ordenada}")

caminho_arquivo_3k = "planilhas/lista3k.xlsx"
lista_3k = carregar_lista_3k(caminho_arquivo_3k)
ordenada, tempo_gasto = medir_tempo_ordenacao(lista_3k)
with open(f"tempoexec/{forma_de_ordenacao}/lista3k.txt", "w") as arquivo:
    arquivo.write("Lista com 3 mil elementos:\n")
    arquivo.write(f"Tempo gasto para ordenar: {tempo_gasto:.6f} segundos\n\n")
    arquivo.write(f"Lista ordenada: {ordenada}")
