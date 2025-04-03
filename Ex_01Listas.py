# EXERCICIOS SOBRE Listas

### Exercicio 1. Crie uma lista com 8 números inteiros e exiba o quinto elemento.
lista = [7, 35, 76, 61, 84, 13, 68, 2]
print(f"Lista com 8 números inteiros: {lista}")
print(f"Exibindo o quinto elemento da lista: {lista[5]}") #Exibe o quinto elemento (indice 5)

### Exercicio 2. Remova todos os números ímpares de uma lista.
lista_pares = [num for num in lista if num % 2 == 0] #Apenas pares
print(f"\nRemovendo os  números ímpares e exibindo apenas apenas os números pares: {lista_pares}")

### Exericicio 3. Crie uma lista com nomes de 5 frutas e verifique se a fruta "Maçã" está presente.
lista_frutas = ["Banana", "Manga", "Maçã", "Lichia", "Ameixa"]
print(f"\nLista com 5 frutas: {lista_frutas}")
print(f"A fruta maçã se encontra na lista de frutas: {"Maçã" in lista_frutas}")

### Exercicio 4. Multiplique todos os elementos da lista por 2 e exiba o resultado.
print(f"\nMultiplicando todos os elementos por 2: {lista * 2}") # Multiplicar por 2

### Exercicio 5. Inverta a ordem dos elementos de uma lista sem usar reverse().
"""O slicing ([::-1]) é uma técnica de fatiamento em Python que cria uma cópia invertida da sequência original. A sintaxe geral é:
sequencia[início:fim:passo]
início: Índice inicial (opcional, padrão = 0).
fim: Índice final (opcional, padrão = último elemento).
passo: Direção e intervalo (negativo inverte a ordem)."""
lista_invertida1 = lista[::-1]  # Passo = -1 (inverte a lista)
print(f"\nLista numerica intertida: {lista_invertida1}")  

# reversed() é uma função embutida que retorna um iterador reverso (não uma lista pronta).
lista_invertida2 = list(reversed(lista_frutas))  # Converte o iterador em lista
print(f"Lista de frutas invertida: {lista_invertida2}")  
