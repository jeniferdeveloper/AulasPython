"""Dicionários
16. Criação e acesso: Crie um dicionário com 3 produtos e seus preços.Acesse o preço de um produto específico.
17. Modificação: Adicione um novo produto e altere o preço de um existente.
18.Remoção: Remova um item do dicionário.
19. Iteração: Percorra o dicionário e exiba cada chave e valor.
20. Conversão: Converta um dicionário para uma lista de tuplas."""

produtos = {
    "Notebook": 3500,
    "Teclado": 150,
    "Mouse": 80
}
print(produtos["Teclado"]) # Exibe o proço do teclado

produtos["Monitor"] = 1200 # Adiciona um novo item
produtos["Notebook"] = 4000 # Altera o preço do Notebook
print(f"\nItens atualizados: {produtos}")

del produtos["Mouse"] # Remove o item Mouse
print(f"\nRemovendo itens: {produtos}")

print("\n") 
for chave, valor in produtos.items():
    print(f"Produtos: {chave}, Preço: R${valor}")

lista_tuplas = list(produtos.items())
print(f"\nConvertendo em lista de tuplas: {lista_tuplas}") # Exibe a conversao em lista de tuplas