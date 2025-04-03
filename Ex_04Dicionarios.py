# EXERCICIOS SOBRE Dicionários

###Exercicio  16.Crie um dicionário com 5 países e suas capitais e exiba a capital do Brasil.
paises = {
    "Bélgica": "Bruxelas",
    "Canadá": "Ottawa",
    "Estados Unidos": "Washington D.C.",
    "México": "Cidade do México",
    "Brasil": "Brasília"
}
print(f"O paises são: {paises}")
print(f"A capital do Brasil é: {paises["Brasil"]}") # Exibe capital do Brasil

### Exercicio 17.Modifique o dicionário alterando a capital de um dos países.
paises["Canadá"] = "Capital alterada" # Alterar a capital de um país
print(f"\nModificando o dicionário: {paises}")

### Exercicio 18. Adicione um novo país e sua capital ao dicionário.
paises["Alemanha"] = "Berlim" # Adiciona um novo país
print(f"\nAdicionando um novo país: {paises}") # Adicionando um novo país

### Exercicio 19. Remova um dos países do dicionário.
del paises["Canadá"] # Remove um páis
print(f"\nRemovendo um país: {paises}")

### Exercicio 20.Converta um dicionário em duas listas, uma com as chaves e outra com os valores.
for chave, valor in paises.items():
    print(f"Países: {chave}, Capital: {valor}")

listas = list(paises.items())
print(f"\nConvertendo em lista: {listas}") # Exibe a conversao em listas
