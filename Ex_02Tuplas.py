# EXERCICIOS SOBRE Tuplas

### Exercicio 6. Crie uma tupla com 6 cidades brasileiras e exiba a última cidade.
tupla = ("Brasília", "Belo Horizonte", "Salvador", "Natal", "Recife", "São Paulo")
print(f"Exibindo a tupla: {tupla}")
print(f"Exibindo a última cidade da tupla: {tupla[5]}") # ultimo indice 

### Exercicio 7. Converta uma tupla para lista, remova um elemento e depois converta novamente para tupla.
lista_temp = list(tupla) # convertendo em Lista
lista_temp.pop(1) # Remove o segundo indice
tupla = tuple(lista_temp) # convertendo em Tupla novamente
print(f"\nLista com um elemento removido: {tupla}")

### Exercicio 8. Crie duas tuplas com 3 cores cada e concatene-as.
tupla1 = ("Azul", "Roxo", "Preto")
tupla2 = ("Vermelho", "Laranja", "Branco")
print(f"\nConcatenado duas tuplas: {tupla1 + tupla2}")

### Exercicio 9. Verifique se a palavra "Python" está presente em uma tupla de linguagens de programação.
print(f"\nA palavra Python se encontra nessa lista: {"Python" in tupla}")
print(f"A palavra Python se encontra nessa lista: {"Python" in tupla1}")
print(f"A palavra Python se encontra nessa lista: {"Python" in tupla2}")

### Exercicio 10.Use index() para encontrar a posição do número 50 em uma tupla de números.
tupla3 = (10,20,30,40,50)
print(f"\nEcontrar o posoção do número 50: {tupla3.index(50)}") # Retorna a posição do numero 50
print(f"Exibindo o número da posição 4: {tupla3[4]}") # Retorna o número da posição 4 que é o numero 50