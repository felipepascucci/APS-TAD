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

# O Selection Sort é um algoritmo de ordenação que funciona da seguinte forma:
# 1- Encontrar o menor: Em cada iteração, o algoritmo encontra o menor elemento não ordenado da lista.
# 2- Trocar de lugar: O menor elemento é trocado de lugar com o primeiro elemento não ordenado.
# 3- Repetir: Esse processo se repete até que toda a lista esteja ordenada.


def selection_sort(arr): 
    for i in range(len(arr)):
        min_index = i  # Define o índice 'min_index' como o índice atual 'i'.
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[min_index]:  # Compara o elemento em 'j' com o elemento no 'min_index'.
                min_index = j  # Se 'arr[j]' for menor, atualiza 'min_index' para o índice 'j'.
        arr[i], arr[min_index] = arr[min_index], arr[i] # Troca o elemento no índice 'i' com o menor elemento encontrado.
    return arr 



def medir_tempo_ordenacao(arr):
    tempo_inicial = time.time()
    ordenada = selection_sort(arr)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial

    return ordenada, tempo_total


# Forma de uso:
forma_de_ordenacao = 'selection-sort'

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
