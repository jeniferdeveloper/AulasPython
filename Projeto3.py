"""Projeto 03 – Jogo da Velha
Criar um jogo da velha interativo onde dois jogadores podem alternar turnos até um deles vencer ou dar empate.
Habilidades trabalhadas:
• Uso de matrizes NumPy para organizar o tabuleiro
• Manipulação de loops e verificações de vitória
• Entrada de dados e interação com o usuário"""

# Importando a biblioteca NumPy, que será utilizada para organizar o tabuleiro do jogo.
import numpy as np

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    """
    Esta função exibe o tabuleiro de jogo na tela.
    
    Parâmetros:
    - tabuleiro: uma matriz 3x3 representando o estado atual do tabuleiro (com "X", "O" ou " ").
    
    A função imprime o tabuleiro de forma legível no console, com separadores entre as linhas e colunas.
    """
    for i in range(3):
        # Exibe uma linha do tabuleiro, unindo as células com '|' e separando as linhas com '---------'
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    """
    Esta função verifica se o jogador (X ou O) venceu o jogo.
    
    Parâmetros:
    - tabuleiro: uma matriz 3x3 representando o estado atual do tabuleiro.
    - jogador: um caractere, 'X' ou 'O', representando o jogador que se deseja verificar.
    
    Retorna:
    - True se o jogador venceu (alinhou três símbolos em linha, coluna ou diagonal).
    - False caso contrário.
    """
    # Verifica se há três símbolos iguais em alguma linha
    for i in range(3):
        if all(tabuleiro[i, j] == jogador for j in range(3)):  # Linha
            return True
        if all(tabuleiro[j, i] == jogador for j in range(3)):  # Coluna
            return True

    # Verifica as duas diagonais
    if tabuleiro[0, 0] == jogador and tabuleiro[1, 1] == jogador and tabuleiro[2, 2] == jogador:  # Diagonal principal
        return True
    if tabuleiro[0, 2] == jogador and tabuleiro[1, 1] == jogador and tabuleiro[2, 0] == jogador:  # Diagonal secundária
        return True
    
    # Se nenhuma condição de vitória for atendida, retorna False
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    """
    Esta função verifica se o jogo terminou em empate. O empate ocorre se o tabuleiro estiver cheio
    e ninguém venceu.
    
    Parâmetros:
    - tabuleiro: uma matriz 3x3 representando o estado atual do tabuleiro.
    
    Retorna:
    - True se o jogo terminou em empate (não há mais espaços vazios e ninguém venceu).
    - False caso contrário.
    """
    # Verifica se há algum espaço vazio no tabuleiro. Se não houver, é um empate
    return not np.any(tabuleiro == " ")

# Função principal que gerencia o fluxo do jogo
def jogar():
    """
    Função principal que gerencia o jogo da velha. Alterna os turnos entre os jogadores X e O, verifica
    as condições de vitória ou empate e exibe o tabuleiro a cada jogada.
    
    O jogo termina quando um dos jogadores vence ou quando o jogo termina em empate.
    """
    # Inicializa o tabuleiro como uma matriz 3x3 vazia (todos os espaços são representados por " ")
    tabuleiro = np.full((3, 3), " ", dtype=str)

    # Define o primeiro jogador como "X"
    jogador_atual = "X"
    
    while True:
        # Exibe o tabuleiro atual na tela
        imprimir_tabuleiro(tabuleiro)
        
        # Solicita a jogada do jogador atual
        print(f"Jogador {jogador_atual}, escolha sua jogada (linha, coluna):")
        
        try:
            # Solicita as coordenadas de linha e coluna do jogador
            linha, coluna = map(int, input("Digite a linha e a coluna (0, 1, 2 separados por espaço): ").split())
            
            # Verifica se a célula selecionada está vazia
            if tabuleiro[linha, coluna] != " ":
                print("Espaço já ocupado! Tente novamente.")
                continue
            
            # Marca a jogada do jogador no tabuleiro
            tabuleiro[linha, coluna] = jogador_atual
            
            # Verifica se o jogador atual venceu após esta jogada
            if verificar_vitoria(tabuleiro, jogador_atual):
                # Exibe o tabuleiro final e a mensagem de vitória
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break  # Finaliza o jogo
            
            # Verifica se o jogo terminou em empate
            if verificar_empate(tabuleiro):
                # Exibe o tabuleiro final e a mensagem de empate
                imprimir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break  # Finaliza o jogo
            
            # Alterna para o próximo jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        
        except (ValueError, IndexError):
            # Se o jogador digitar um valor inválido (não numérico ou fora dos limites 0-2), exibe uma mensagem de erro
            print("Entrada inválida! Digite as coordenadas corretamente (valores entre 0 e 2).")

# Inicia o jogo chamando a função principal
jogar()