"""6. Criação e acesso: Crie uma tupla com 4 nomes e exiba o segundo nome.
   7. Conversão: Converta uma tupla para uma lista, altere um valor e converta de volta para tupla.
   8. Verificação: Verifique se um determinado valor existe dentro da tupla.
   9. Concatenação: Crie duas tuplas e una ambas em uma nova tupla.
   10. Indexação: Use index() para encontrar a posição de um elemento na tupla."""

#6. Criação e acesso: Crie uma tupla com 4 nomes e exiba o segundo nome.
tupla = ("Alice", "Bruno", "Carlos", "Daniela")
print(tupla[1]) # Segundo nome (indice 1)

#7. Conversão: Converta uma tupla para uma lista, altere um valor e converta de volta para tupla.
lista_temp = list(tupla)
lista_temp[2] = "Clara"
tupla = tuple(lista_temp)
print(tupla)


# 8. Verificação: Verifique se um determinado valor existe dentro da tupla.
print("Daniela" in tupla) # Retorna True ou False

#9. Concatenação: Crie duas tuplas e una ambas em uma nova tupla.
tupla1 = ("Jorge", "Matheus", 20, 50)
tupla2 = (1, "Luana", "Joao", 90)

tupla3 = tupla1 + tupla2
#concatenar = tupla1 + tupla2
print(tupla3)
# outras maneiras
# print(tupla1 + tupla2)

#10. Indexação: Use index() para encontrar a posição de um elemento na tupla.
print(tupla3.index("Matheus")) # Retorna a posição do nome Matheus
print(tupla3[4])