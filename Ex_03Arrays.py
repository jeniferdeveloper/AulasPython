# EXERCICIOS SOBRE Arrays (NumPy)

import numpy as np # importando o numpy declarando como np

### Exercicio 11.Crie um array NumPy com 10 números aleatórios entre 1 e 100.
array = np.array([30, 97, 59, 69, 10, 58, 22, 25, 90, 56])
print(f"Exibindo a array: {array}")

### Exercicio 12.Multiplique todos os elementos do array por -1, tornando-os negativos.
print(f"\nMultiplicando a array por -1: {array * -1}") # Multiplicar por -1

### Exercicio 13. Substitua todos os números maiores que 50 por 50.
# O np.where() é uma função poderosa do NumPy que permite fazer seleções condicionais em arrays de forma eficiente.
# np.where(condição, valor_se_verdadeiro, valor_se_falso)
# Ótimo para operações do tipo "substitua X por Y onde Z é verdadeiro"
array_modificada = np.where(array >= 50, 50, array)  # Substitui >= 50 por 50
print(f"\nSubistituindo os números maiores que 50 por 50: {array_modificada}")  

### Exercicio 14.Crie dois arrays NumPy e encontre a diferença entre seus elementos.
# Criando dois arrays NumPy
array1 = np.array([27, 33, 48, 13, 30])
array2 = np.array([41, 3, 16, 20, 7])

# OBS: Os arrays devem ter o mesmo tamanho para que a operação de subtração seja realizada elemento por elemento.
print(f"\nExibindo o Array 1: {array1}")
print(f"Exibiindo o Array 2:", array2)
print(f"Diferença entre os elementos do array1 e array2: {array1 - array2}") # Calculando a diferença entre os elementos (array1 - array2)
print(f"Diferença entre os elementos do array1 e array2 usando np.subtract: {np.subtract(array1, array2)}") # Calculando a diferença entre os elementos (array1 - array2) usando np.subtract

### Exercicio 15. Encontre o menor e o maior valor dentro de um array.
menor = np.min(array)
maior = np.max(array)
print(f"\nMenor valor: {menor} e Maior valor: {maior}") # Exibe menor e maior valor