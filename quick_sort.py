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

# O Quick Sort é um algoritmo de ordenação que funciona da seguinte forma:
# 1- Escolher um pivô: Um elemento da lista é escolhido como pivô.
# 2- Particionamento: Os elementos menores que o pivô são colocados à esquerda e os maiores, à direita.
# 3- Recursão: O processo é repetido para as sublistas à esquerda e à direita do pivô.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Escolhe o elemento do meio como pivot
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivot
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivot
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivot
        return quick_sort(left) + middle + quick_sort(right)  # Recursão


def medir_tempo_ordenacao(arr):
    tempo_inicial = time.time()
    ordenada = quick_sort(arr)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial

    return ordenada, tempo_total


# Forma de uso:
forma_de_ordenacao = 'quick-sort'

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
