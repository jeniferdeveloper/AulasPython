
"""Arrays (NumPy)
11. Criação e soma: Crie um array NumPy com 5 números e some 2 a cada elemento.
12. Multiplicação: Multiplique todos os elementos do array por 3.
13. Soma de arrays: Crie dois arrays e some os elementos correspondentes.
14. Média e desvio padrão: Calcule a média e o desvio padrão de um array.
15. Filtragem: Exiba apenas os números pares do array."""

import numpy as np
array = np.array([10,20,30,40,50])
print(f"Somar 2 a cada elemento: {array + 2}") # Adiciona 2 a cada elemento

print(f"\nMultiplicar por 3 cada elemento: {array * 3}") # Multiplicar por 3

array2 = np.array([1,2,3,4,5])
print(f"\nSomar dois arrays: {array + array2}") # Soma os arrays

print("\nMédia: ", np.mean(array)) # Calcula a média aritmética dos valores no array.
print("Desvio padrão: ", np.std(array)) # Calcula o desvio padrão, que mede a dispersão dos dados em relação à média. (dispersão dos dados)

print("\nImprima apenas os números pares: ", array[array % 2 == 0]) #Apenas pares