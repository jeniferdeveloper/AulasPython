### Atividades sobre Matrizes em Python
## Parte 1: Matrizes com Listas Aninhadas

import numpy as np

### 1. Criar uma matriz 3x3 e imprimir todos os elementos.
print("Exercicio 1")
# Matriz 3x3 usando lista aninhadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Imprimindo a matriz 3x3 e todos seus elementos: ")
# Percorrendo a matriz e imprimindo os valores
for linha in matriz: # Percorre cada linha (sublista) da matriz
    for elemento in linha: # Percorre cada elemento dentro da linha atual
        print(elemento, end=" ")  # Imprime o elemento, seguido de um espaço (sem quebra de linha)
    print()  # Quebra a linha após imprimir todos os elementos de uma linha

### 2. Criar uma matriz 4x4 e acessar o elemento da segunda linha e terceira coluna.
print("\nExercicio 2")
matriz_2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Imprimindo segunda matriz 4x4: ")
for linha in matriz_2: # Percorre cada linha (sublista) da matriz
    for elemento in linha: # Percorre cada elemento dentro da linha atual
        print(elemento, end=" ")  # Imprime o elemento, seguido de um espaço (sem quebra de linha)
    print()

# Acessando um elemento (linha 2, coluna 3)
print("Elemento na posição (2,3):", matriz_2[2][3])

### 3. Criar uma matriz identidade 3x3 manualmente usando listas aninhadas.
    # Uma matriz identidade é uma matriz quadrada em que todos os elementos da diagonal principal são 1 e os demais elementos são 0.
print("\nExercicio 3")
matriz_identidade = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print("Impriminindo matriz identidade:")
# Imprimir a matriz
for linha in matriz_identidade:
    print(linha)

### 4. Criar uma matriz 3x3 e calcular a soma de todos os elementos.
print("\nExercicio 4")
matriz_np = np.array ([
    [1, 6, 8],
    [10, 11, 16],
    [17, 18, 20]
])
 	  	
print("Impriminindo matriz_np:")
# Imprimir a matriz
for linha in matriz_np:
    print(linha)

print("Soma dos elementos da matriz_np:", np.sum(matriz_np))

### 5. Criar uma matriz 3x3 e exibir apenas os elementos da diagonal principal.
    # Diagonal principal: Os elementos da diagonal principal são aqueles em que o índice da linha é igual ao índice da coluna 
    # (matriz[0][0], matriz[1][1], matriz[2][2]).
    # Compreensão de lista: Usamos [matriz[i][i] for i in range(3)] para coletar os elementos onde i (linha) é igual a j (coluna).
print("\nExercicio 5")
matriz_5 = [
    [8, 10, 12],
    [14, 55, 16],
    [17, 18, 25]
]

print("Impriminindo matriz_5:")
# Imprimir a matriz
for linha in matriz_5:
    print(linha)

# Extrair e exibir os elementos da diagonal principal
diagonal_principal = [matriz_5[i][i] for i in range(3)]
print("Elementos da diagonal principal:", diagonal_principal)

### 6. Criar uma matriz 3x3 e exibir apenas os elementos da diagonal secundária.
    # a diagonal secundária é composta pelos elementos onde a soma do índice da linha e da coluna é igual a 2 
    # (ou n-1, onde n é o tamanho da matriz).
    # matriz[0][2] (linha 0, coluna 2 → 0 + 2 = 2)
    # matriz[1][1] (linha 1, coluna 1 → 1 + 1 = 2)
    # matriz[2][0] (linha 2, coluna 0 → 2 + 0 = 2)
print("\nExercicio 6")

matriz_6 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Impriminindo matriz_6:")
# Imprimir a matriz
for linha in matriz_6:
    print(linha)

# Extrair os elementos da diagonal secundária
diagonal_secundaria = [matriz_6[i][2 - i] for i in range(3)]
# Exibir resultado
print("Elementos da diagonal secundária:", diagonal_secundaria)

### 7. Criar uma matriz 3x3 e inverter a ordem das linhas.
print("\nExercicio 7")

matriz_7 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

print("Impriminindo matriz_7:")
# Imprimir a matriz
for linha in matriz_7:
    print(linha)

# Inverte a matriz (altera a original)
matriz_7.reverse()

print("\nImpriminindo matriz_7 invertida:")
# Exibe a matriz invertida
for linha in matriz_7:
    print(linha)

### 8. Criar uma matriz 3x3 e calcular a média dos elementos.
print("\nExercicio 8")

print("Usando a matriz_np do exercício 4.")

print("Média dos valores da matriz_np:", np.mean(matriz_np))


### 9. Criar uma matriz 3x3 e encontrar o maior e o menor elemento.
print("\nExercicio 9")
matriz_9 = [
    [15, 23, 8],
    [4, 42, 16],
    [7, 3, 20]
]

print("Impriminindo matriz_9:")
for linha in matriz_9:
    print(linha)

# Encontrando o maior e o menor elemento da matriz
maior_elemento = max(max(linha) for linha in matriz_9)  # max() em cada linha e depois o max() geral
# max(linha) encontra o maior valor de cada linha. max(max(linha) for linha in matriz) encontra o maior valor em todas as linhas.
menor_elemento = min(min(linha) for linha in matriz_9)  # min() em cada linha e depois o min() geral
#  min(linha) encontra o menor valor de cada linha, e min(min(linha) for linha in matriz) encontra o menor valor em todas as linhas.

# Exibindo os resultados
print("\nMaior elemento:", maior_elemento)
print("Menor elemento:", menor_elemento)

### 10. Criar uma matriz 4x4 e verificar se um determinado número existe nela.
print("\nExercicio 10")

print("Impriminindo matriz_2:")
# usando a matriz do exercicio 2.
for linha in matriz_2:
    print(linha)

# Número a ser buscado
numero = int(input("\nDigite um número para buscar na matriz: "))

# Verifica se o número existe em qualquer linha da matriz
encontrado = any(numero in linha for linha in matriz_2)
# any() retorna True se pelo menos um elemento do loop for verdadeiro.
# numero in linha verifica se o número está presente em uma linha específica.

# 2 Lógicas para a solução do exercicio   
"""# Variável para verificar se o número foi encontrado
encontrado = False

# Percorrer a matriz
for linha in matriz_2:
    for elemento in linha:
        if elemento == numero:
            encontrado = True
            break  # Sai do loop interno se encontrar
    if encontrado:
        break  # Sai do loop externo se encontrar"""

# Resultado
if encontrado:
    print(f"O número '{numero}' está na matriz!")
else:
    print(f"O número '{numero}' NÃO está na matriz.")