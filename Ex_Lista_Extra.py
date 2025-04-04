# Lista Extra Python

### Exercicio 1. Contando Letras
#João está aprendendo a programar e precisa criar um programa que peça ao usuário para digitar uma palavra e mostre quantas letras essa palavra tem.

# Solicita ao usuário que digite uma palavra
print("Exercicio 1. Contando Letras")
palavra = input("Digite uma palavra: ")

# Calcula o número de letras na palavra
quantidade_letras = len(palavra)

# Mostra o resultado
print(f"A palavra '{palavra}' tem {quantidade_letras} letras.")

### Exercicio 2. Dobro e Metade
# Você foi contratado para fazer um programa que receba um número do usuário e mostre o dobro e a metade desse número.

# Solicita ao usuário que digite um número
print("\nExercicio 2. Dobro e Metade")
numero = float(input("Digite um número: "))

# Calcula o dobro do numero
dobro = numero * 2
print(f"O dobro do número '{numero}' é: {dobro}")

# Calcula a metade do numero
metade = numero / 2
print(f"A metade do número '{numero}' é: {metade}")

### Exercicio 3. Par ou Ímpar?
# Crie um programa que receba um número e informe se ele é par ou ímpar.
print("\nExercicio 3. Par ou Ímpar?")

if numero % 2 == 0: 
    print(f"O número '{numero}' é par")
else:
   print(f"O número '{numero}' é ímpar") 

### Exercicio 4. Contagem Progressiva
# A empresa Contagem Rápida precisa de um programa que exiba os números de 1 a 10, um por linha.
print("\nExercicio 4. Contagem Progressiva")

# Programa que exibe números de 1 a 10, um por linha
print("Números de 1 a 10:")
for num in range(1, 11):
    print(num)

### Exercicio 5.Média Simples
# Faça um programa que receba três números do usuário e calcule a média aritmética deles.
print("\nExercicio 5. Média Simples")

# Solicita ao usuário que digite um número
numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))
numero3 = float(input("Digite o 3º número: "))

media = (numero1 + numero2 + numero3) / 3

print(f"A média dos 3 números digitados é: {media}")

### Exercicio 6. Lista de Tarefas
# Maria quer organizar sua rotina. Escreva um programa que permita ao usuário adicionar três tarefas em uma lista e depois exibi-las na tela.

# Programa para organizar tarefas
print("\nExercicio 6. Lista de Tarefas da Maria")

# Cria uma lista vazia para armazenar as tarefas
tarefas = []

# Pede ao usuário para digitar 3 tarefas
for i in range(3):
    tarefa = input(f"Digite a {i+1}ª tarefa: ")
    tarefas.append(tarefa)  # Adiciona a tarefa à lista

# Exibe as tarefas organizadas
print("\nLista de Tarefas da Maria:")
for i, tarefa in enumerate(tarefas, start=1): # Exibe todas as tarefas numeradas usando outro loop for
    print(f"{i}. {tarefa}")

### Exercicio 7. Nome ao Contrário
# Carlos está aprendendo sobre strings. Ele precisa criar um programa que peça o nome do usuário e o exiba invertido (Exemplo: "Carlos" → "solraC").
print("\nExercicio 7. Nome ao Contrário")

# Programa que inverte um nome
nome = input("Digite seu nome: ")

"""O slicing ([::-1]) é uma técnica de fatiamento em Python que cria uma cópia invertida da sequência original. A sintaxe geral é:
sequencia[início:fim:passo]
início: Índice inicial (opcional, padrão = 0).
fim: Índice final (opcional, padrão = último elemento).
passo: Direção e intervalo (negativo inverte a ordem)."""
# Inverte o nome usando slicing
nome_invertido = nome[::-1]
print(f"Seu nome invertido é: {nome_invertido}")

### Exercicio 8. Tabuada Automática
# Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10.
print("\nExercicio 8. Tabuada Automática")

# Lendo o número inteiro positivo
numero = int(input("Digite um número inteiro positivo entre 1 e 10: "))

# Verificando se o número é positivo
if numero > 0:
    # Exibindo a tabuada do número de 1 a 10
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}") 
        # {numero} x {i} = exibe na tela qual numero esta sendo multiplicado (2 x 5) e {numero * i} faz a multiplicação
else:
    print("Por favor, digite um número inteiro positivo.")

### Exercicio 9. Desconto na Loja
# Uma loja quer oferecer 10% de desconto para os clientes. Faça um programa que receba o valor de um produto e calcule o novo preço com o desconto.
print("\nExercicio 9. Desconto na Loja")

# Solicita o preço do produto
produto = float(input("Digite o preço do produto: "))

# Calcula 10% do produto
desconto = produto - (produto * 0.10) 

# Exibe o resultado
print(f"Produto com desconto: R${desconto}")

### Exercicio 10. Números Pares
# Escreva um programa que mostre todos os números pares de 0 a 20.
print("\nExercicio 10. Números Pares")

print("Números pares de 0 a 20:")
for numero in range(21):
    if numero % 2 == 0:  # Verifica se o número é par
        print(numero)

### Exercicio 11. Controle de Temperatura
#Imagine que você trabalha no setor de meteorologia. Faça um programa que receba 5 temperaturas diárias e informe a temperatura média, a maior e a
#menor.
print("\nExercicio 11. Controle de Temperatura")

# Inicializa uma lista vazia para armazenar as temperaturas
temperaturas = []

# Solicita as 5 temperaturas ao usuário
for i in range(5):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

# Calcula as estatísticas
media = sum(temperaturas) / len(temperaturas)
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)

# Exibe os resultados
print("\nResultados:")
print(f"Temperaturas registradas: {temperaturas}")
print(f"Média das temperaturas: {media:.1f}°C")
print(f"Maior temperatura: {maior_temp}°C")
print(f"Menor temperatura: {menor_temp}°C")

### Exercicio 12.Gerenciador de Estoque
"""Um supermercado precisa controlar seu estoque. Escreva um programa que:
• Permita ao usuário adicionar 3 produtos e seus respectivos preços a um dicion ário.
• Depois, exiba os produtos cadastrados e seus preços."""

print("\nExercicio 12.Gerenciador de Estoque")

# Cria um dicionário vazio para armazenar os produtos
estoque = {}

# Cadastra 3 produtos
for i in range(3):
    print(f"\nCadastro do {i+1}º produto:") # solicita 3 vezes o nome e preço de cada produto
    produto = input("Nome do produto: ").strip().title() # strip() e title() formatam o nome do produto (remove espaços extras e coloca em título)
    preco = float(input("Preço do produto: R$ "))
    estoque[produto] = preco  # Os valores são armazenados no dicionário estoque onde a chave é o nome do produto e o valor é o preço

# Exibe o estoque completo
print("\n===== ESTOQUE  =====")
print("{:<15} {:<10}".format('PRODUTO', 'PREÇO'))  
""" "{:<15} {:<10}" é uma string de formatação que define:
Primeiro campo ({:<15}): ocupa 15 caracteres, alinhado à esquerda (<)
Segundo campo ({:<10}): ocupa 10 caracteres, alinhado à esquerda (<)
.format('PRODUTO', 'PREÇO') preenche os campos com as palavras "PRODUTO" e "PREÇO".""" 
print("-" * 25) #Cria uma linha com 25 hífens para separar o cabeçalho dos dados.
for produto, preco in estoque.items(): # estoque.items() retorna pares (produto, preco) do dicionário.
    print("{:<15} R$ {:<8.2f}".format(produto, preco))  
    """"{:<15} R$ {:<8.2f}" define:
    Primeiro campo ({:<15}):
    Alinhamento à esquerda (<) em 15 caracteres para o nome do produto.
    Texto fixo (R$ ):
    Adiciona o símbolo "R$ " antes do preço.
    Segundo campo ({:<8.2f}):
    Alinhamento à esquerda (<) em 8 caracteres no total.
    Formatação .2f para exibir o preço com 2 casas decimais."""


### Exercicio 13. Fila do Atendimento
"""Um hospital quer organizar a fila de atendimento. Crie um programa que:
• Peça nomes de pacientes e os adicione a uma lista.
• Depois, exiba a ordem de atendimento.
• Quando um paciente for atendido, remova-o da fila."""

print("\nExercicio 13. Fila do Atendimento")

# Programa de gestão de fila hospitalar
fila_atendimento = []

print("=== CONTROLE DE FILA HOSPITALAR ===")
print("Digite 'fim' para encerrar a entrada de pacientes\n")

# Adiciona pacientes à fila
while True:
    paciente = input("Nome do paciente (ou 'fim' para encerrar): ").strip().title()
    if paciente.lower() == 'fim':
        break
    fila_atendimento.append(paciente)
    print(f"{paciente} foi adicionado à fila.")

# Mostra a fila atual
def mostrar_fila():
    print("\n--- Fila de Atendimento ---")
    if not fila_atendimento:
        print("Fila vazia.")
    else:
        for i, paciente in enumerate(fila_atendimento, 1):
            print(f"{i}º - {paciente}")

# Processo de atendimento
while fila_atendimento:
    mostrar_fila()
    input("\nPressione Enter para chamar o próximo paciente...")
    atendido = fila_atendimento.pop(0)
    print(f"\n--> {atendido} está sendo atendido agora.")

print("\nTodos os pacientes foram atendidos!")

