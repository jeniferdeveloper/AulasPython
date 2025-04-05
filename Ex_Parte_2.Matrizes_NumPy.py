### Parte 2: Matrizes com NumPy

import numpy as np

### 11. Criar uma matriz NumPy 3x3 e exibir sua transposta.
print("\nExercicio 11")
matriz_np = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Matriz Numpy:\n", matriz_np)

print("\nA matriz transposta troca as linhas pela colunas")
print("Transposta da matriz:\n", matriz_np.T) # TRANSPOSTA: troca as linhas pela colunas

""" A matriz transposta é uma matriz obtida pela troca das linhas pelas colunas da matriz original. 
Em outras palavras, se a matriz original é A, sua transposta é denotada por Aᵀ (ou A'), onde:
A linha i da matriz original vira a coluna i da matriz transposta.
A coluna j da matriz original vira a linha j da matriz transposta."""

### 12. Criar uma matriz 4x4 de zeros usando np.zeros().
print("\nExercicio 12")
print("Matriz Zerada")
matriz_zero = np.zeros((4,4))
print(matriz_zero)

### 13. Criar uma matriz 4x4 de uns usando np.ones().
    # A função np.ones() cria um array preenchido com o valor 1.
print("\nExercicio 13")

# Criar uma matriz 4x4 de uns
matriz_ones = np.ones((4, 4)) # (4 linhas e 4 colunas).

# Exibir a matriz
print("Matriz 4x4 usando o ones():")
print(matriz_ones)

"""Se quiser preencher com outro valor (ex: 5), use np.full():
    matriz_cinco = np.full((4, 4), 5)"""

### 14. Criar uma matriz NumPy 3x3 com valores aleatórios entre 1 e 50.
print("\nExercicio 14")

matriz_rand = np.random.randint(1, 51, (3,3))
print("Matriz 3x3 com valores aleatórios entre 1 e 50\n", matriz_rand)

### 15. Criar duas matrizes 3x3 e somá-las.
print("\nExercicio 15")
matriz_1 = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matriz_2 = np.array ([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

print("Matriz 1:\n", matriz_1)
print("\nMatriz 2:\n", matriz_2)

soma_matriz = matriz_1 + matriz_2
print(f"\nSoma das matrizes:\n {soma_matriz}")

### 16. Criar uma matriz 3x3 e multiplicar todos os elementos por um número fixo.
print("\nExercicio 16")
print("Matriz 1:\n", matriz_1)

# Multiplicando por 2
multi_matriz = matriz_1 * 2  # Ou: multi_matriz = np.multiply(matriz_1, 2)
print(f"\nMultiplicando matriz por 2:\n {multi_matriz}")

### 17. Criar uma matriz 3x3 e dividir todos os elementos por 2.
print("\nExercicio 17")
print("Matriz 1:\n", matriz_1)

# Dividindo por 2
div_matriz = matriz_1 / 2  # Ou: div_matriz = np.divide(matriz_1, 2)
print(f"\nDivindo matriz por 2:\n {div_matriz}")

### 18. Criar uma matriz 3x3 e calcular seu determinante (np.linalg.det).
print("\nExercicio 18")
matriz_3 = np.array([
    [4, 2, 1],
    [3, 0, 5],
    [7, 8, 6]
])

print("Matriz 3:\n", matriz_3)

# Calcular o determinante
determinante = np.linalg.det(matriz_3)

print(f"\nDeterminante da matriz: {round(determinante, 2)}") # arredondar o resultado

### 19. Criar uma matriz 4x4 e calcular a soma das colunas (np.sum(matriz,axis=0)).
print("\nExercicio 19")
matriz_4 = np.array([
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
])

print("Matriz 4:\n", matriz_4)
# Calcular a soma de cada coluna (axis=0)
soma_colunas = np.sum(matriz_4, axis=0) # axis=0 significa "ao longo das linhas" (soma vertical)

print(f"\nSoma de cada coluna: {soma_colunas}")

### 20. Criar uma matriz 4x4 e calcular a soma das linhas (np.sum(matriz,axis=1)).
print("\nExercicio 20")

print("Matriz 4:\n", matriz_4)
# Calcular a soma de cada coluna (axis=1)
soma_linhas = np.sum(matriz_4, axis=1) # axis=1 significa "ao longo das colunas" (soma horizontal)

print(f"\nSoma de cada linha: {soma_linhas}")