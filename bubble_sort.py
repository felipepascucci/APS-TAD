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

# O Bubble Sort é um algoritmo de ordenação que funciona da seguinte forma:
# 1- Comparar adjacentes: Em cada iteração, compara-se cada elemento com seu vizinho imediato.
# 2- Trocar se necessário: Se o elemento da esquerda for maior que o da direita, eles são trocados de lugar.
# 3- Repetir: Esse processo se repete até que a lista esteja ordenada.


def bubble_sort(arr):  
    n = len(arr)
    
    for i in range(n):  
        change = False 

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  # Compara o elemento atual 'arr[j]' com o próximo 'arr[j+1]'.
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Se 'arr[j]' for maior, troca os dois elementos.
                trocou = True  # Define 'trocou' como True, indicando que houve uma troca.

        if not change:
            break

    return arr



def medir_tempo_ordenacao(arr):
    tempo_inicial = time.time()
    ordenada = bubble_sort(arr)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial

    return ordenada, tempo_total


# Forma de uso:
forma_de_ordenacao = 'bubble-sort'

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
