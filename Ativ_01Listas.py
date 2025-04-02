# 1. Criar uma lista e acessar um elemento
# 2. Modificar um elemento da lista
# 3. Adicione um número ao final da lista e remova o primeiro número.
# 4. Ordene a lista em ordem crescente e decrescente.
# 5. Calcule a soma e a média dos valores da lista.

lista = [10,20,30,40,50]
print(f"Lista inicial: {lista}")
print(lista[2]) #Exibe o terceiro elemento (indice 2)

lista[1] = 99 # Subistitui o segundo elemento (indice 1) por 99
print(f"Lista com elemento modificado: {lista}")

lista.append(60) # Adiciona 60 ao final
lista.pop(0) # Remove o primeiro indice
print(f"Lista após a remoção e adição de um elemento: {lista}")

lista.sort() # Ordem crescente
print(f"Lista em ordem crescente: {lista}")

lista.sort(reverse=True) # Ordem decrescente
print(f"Lista em ordem decrescente: {lista}")

#Soma e media das listas
lista = [10,20,30,40,50]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, média: {media}")



