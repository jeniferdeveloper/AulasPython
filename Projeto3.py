"""Projeto 03 – Jogo da Velha
Criar um jogo da velha interativo onde dois jogadores podem alternar turnos até um deles vencer ou dar empate.
Habilidades trabalhadas:
• Uso de matrizes NumPy para organizar o tabuleiro
• Manipulação de loops e verificações de vitória
• Entrada de dados e interação com o usuário"""

# Importando a biblioteca NumPy, que será utilizada para organizar o tabuleiro do jogo.
import numpy as np

def criar_tabuleiro():
    """Cria um tabuleiro vazio 3x3.
    
    Retorna:
        np.ndarray: Uma matriz 3x3 preenchida com espaços vazios (' '), representando o tabuleiro do jogo.
    """
    # cria uma matriz 3x3 (tabuleiro do jogo da velha) preenchida com espaços em branco (' '), representando células vazias.
    return np.full((3, 3), ' ') # A função np.full() é uma função da biblioteca NumPy que cria um array (ou matriz) com um tamanho especificado e preenche todos os seus elementos com um valor específico.

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro de jogo na tela.
    
    Parâmetros:
        tabuleiro (np.ndarray): Uma matriz 3x3 representando o estado atual do tabuleiro (com "X", "O" ou " ").
    """
    print("\n  0   1   2")  # Índices das colunas
    for i, linha in enumerate(tabuleiro):
        # Imprime cada linha com a formatação adequada
        print(f"{i} {linha[0]} | {linha[1]} | {linha[2]}")  # Índice da linha
        if i < 2:
            print("  ---------")  # Linha divisória para melhorar a legibilidade

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador (X ou O) venceu o jogo.
    
    Parâmetros:
        tabuleiro (np.ndarray): Uma matriz 3x3 representando o estado atual do tabuleiro.
        jogador (str): Um caractere ('X' ou 'O') representando o jogador que se deseja verificar.
        
    Retorna:
        bool: True se o jogador venceu (alinhou três símbolos em linha, coluna ou diagonal),
              False caso contrário.
    """
    # Verifica se há três símbolos iguais em alguma linha
    for i in range(3):
        # A função all() no seu código é usada para verificar se todas as células em uma linha, coluna ou diagonal do tabuleiro possuem o mesmo valor, indicando que um jogador venceu, alinhando seus símbolos.
        if all(tabuleiro[i, j] == jogador for j in range(3)):  # Linha
            return True
        if all(tabuleiro[j, i] == jogador for j in range(3)):  # Coluna
            return True

    # Verifica as duas diagonais
    if tabuleiro[0, 0] == jogador and tabuleiro[1, 1] == jogador and tabuleiro[2, 2] == jogador:  # Diagonal principal
        return True
    if tabuleiro[0, 2] == jogador and tabuleiro[1, 1] == jogador and tabuleiro[2, 0] == jogador:  # Diagonal secundária
        return True
    
    return False  # Caso contrário, não houve vitória

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    """
    Verifica se o jogo terminou em empate. O empate ocorre se o tabuleiro estiver cheio
    e ninguém venceu.
    
    Parâmetros:
        tabuleiro (np.ndarray): Uma matriz 3x3 representando o estado atual do tabuleiro.
        
    Retorna:
        bool: True se o jogo terminou em empate, ou seja, se não houver espaços vazios e ninguém venceu.
              False caso contrário.
    """
    # Verifica se há algum espaço vazio no tabuleiro. Se não houver, é um empate
    return not np.any(tabuleiro == " ")  # Se não houver espaços vazios, retorna True (empate)

# Função principal que gerencia o fluxo do jogo
def jogar():
    """Controla o fluxo do jogo da velha.
    
    Inicializa o tabuleiro, alterna entre os jogadores, recebe as entradas dos jogadores, verifica as condições de vitória e empate.
    """
    # Inicializa o tabuleiro como uma matriz 3x3 vazia (todos os espaços são representados por " ")
    tabuleiro = criar_tabuleiro()

    # Define o primeiro jogador como "X"
    jogador_atual = "X"

    print("\nBem-vindo ao Jogo da Velha!")
    print("\nInstruções:")
    print("- Digite as coordenadas no formato 'linha,coluna' separados por ',' (ex: 0,1)")
    print("- Linhas e colunas são numeradas de 0 a 2")
    print("- Jogador X começa, seguido pelo jogador O\n")

    while True:
        # Exibe o tabuleiro atualizado
        imprimir_tabuleiro(tabuleiro)

        # Obtém a jogada do jogador com tratamento de erros
        try:
            # Solicita a entrada do jogador no formato linha,coluna
            entrada = input(f"Jogador {jogador_atual}, digite linha,coluna separados por ',' (ex: 0,1): ")
            linha, coluna = map(int, entrada.split(','))  # Converte a entrada para inteiros

            # Verifica se a posição está dentro dos limites (0 a 2 para linhas e colunas)
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida! Digite valores entre 0 e 2.")
                continue  # Se a posição for inválida, solicita novamente a jogada
            
            # Verifica se a célula selecionada está vazia
            if tabuleiro[linha, coluna] != " ":
                print("Espaço já ocupado! Tente novamente.")
                continue  # Se a posição já estiver ocupada, solicita novamente a jogada

            # Marca a jogada do jogador no tabuleiro
            tabuleiro[linha, coluna] = jogador_atual
            
            # Verifica se o jogador atual venceu após esta jogada
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break  # Finaliza o jogo
            
            # Verifica se o jogo terminou em empate
            if verificar_empate(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break  # Finaliza o jogo
            
            # Alterna para o próximo jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        
        except (ValueError, IndexError):
            # Se o jogador digitar um valor inválido (não numérico ou fora dos limites 0-2), exibe uma mensagem de erro
            print("Entrada inválida! Digite as coordenadas corretamente (valores entre 0 e 2).")

# Inicia o jogo chamando a função principal
if __name__ == "__main__":
    jogar()

"""
O bloco if __name__ == "__main__": permite que o código que está dentro dele seja executado somente quando o arquivo for 
executado diretamente, e não quando for importado em outro script. Isso é útil para evitar a execução de partes do código 
indesejadas (como iniciar o jogo) quando o script é usado como um módulo em outro programa.

Se você remover o bloco if __name__ == "__main__": e chamar diretamente a função jogar() em seu código, ele ainda funcionará 
enquanto você estiver executando o arquivo diretamente. No entanto, há algumas considerações sobre como isso pode impactar o 
comportamento, dependendo de como o script é executado.

"""