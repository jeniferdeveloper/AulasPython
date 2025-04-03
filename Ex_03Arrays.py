"""Arrays (NumPy)
11.Crie um array NumPy com 10 números aleatórios entre 1 e 100.
12.Multiplique todos os elementos do array por -1, tornando-os negativos.
13. Substitua todos os números maiores que 50 por 50.
14.Crie dois arrays NumPy e encontre a diferença entre seus elementos.
15. Encontre o menor e o maior valor dentro de um array."""

import numpy as np

array = np.array([30, 97, 59, 69, 10, 58, 22, 25, 90, 56])
print(f"Exibindo a array: {array}")

print(f"\nMultiplicando a array por -1: {array * -1}") # Multiplicar por -1

# O np.where() é uma função poderosa do NumPy que permite fazer seleções condicionais em arrays de forma eficiente.
# np.where(condição, valor_se_verdadeiro, valor_se_falso)
# Ótimo para operações do tipo "substitua X por Y onde Z é verdadeiro"
array_modificada = np.where(array >= 50, 50, array)  # Substitui >= 50 por 50
print(f"\nSubistituindo os números maiores que 50 por 50: {array_modificada}")  

# Exibe menor e maior valor
menor = np.min(array)
maior = np.max(array)
print(f"\nMenor valor: {menor} e Maior valor: {maior}")  