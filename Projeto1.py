"""Projeto 01 - Calculadora Interativa
Criar uma calculadora que realiza as 4 operações básicas (+, -, *, /) e aceita múltiplos cálculos em sequência.
Habilidades trabalhadas:
• Manipulação de entrada de usuário (input( ))
• Uso de funções para organizar o código
• Laços (while) e condicionais (if)"""

# Funções para as operações básicas
# São definidas funções simples (somar, subtrair, multiplicar, dividir) que recebem dois parâmetros e retornam o resultado da operação.
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0: 
        return a / b
    else:
        return "Erro: Divisão por zero não permitida."

# Função principal
# Dentro da função principal, um loop while permite que o usuário insira múltiplos cálculos até digitar 'sair' para encerrar o programa.
def calculadora():
    while True:
       
        # Para evitar erros ao inserir dados inválidos, usamos try e except para capturar entradas que não sejam números válidos.
        try:
            num1 = float(input("Digite o primeiro número: "))  # Solicitar o primeiro número
        except ValueError: # saida erro
            print("Entrada inválida. Por favor, digite um número.")
            continue

        # Solicitar a operação
        operacao = input("Escolha a operação (+, -, *, /) ou 'sair' para finalizar: ").strip() # O strip() garante que, se o usuário digitar espaços extras antes ou depois da operação (por exemplo, " + " ou " * "), esses espaços sejam removidos antes de compararmos a operação.

        # Verificar se o usuário quer sair
        if operacao.lower() == 'sair':
            print("Saindo da calculadora...")
            break

        # A função lower() é aplicada à entrada do usuário (armazenada em operacao). Isso serve para garantir que, 
        # independentemente de o usuário digitar "SAIR", "sair", "Sair" ou qualquer outra variação de maiúsculas e minúsculas, 
        # o programa considere o comando como 'sair' (em minúsculas). 
        
        try:
            num2 = float(input("Digite o segundo número: ")) # Solicitar o segundo número
        except ValueError:  # saida erro
            print("Entrada inválida. Por favor, digite um número.")
            continue

        # Realizar a operação escolhida
        # A operação escolhida pelo usuário é verificada através de uma estrutura condicional (if, elif). 
        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operação inválida. Tente novamente.") # Se o usuário escolher uma operação inválida, o programa informa e solicita uma nova entrada.
            continue

        # Exibir o resultado
        print(f"Resultado: {resultado}")

# Chamar a função principal para rodar a calculadora
# O programa imprime o resultado do cálculo imediatamente após cada operação e permite que o usuário continue realizando cálculos até escolher 'sair'.
calculadora()