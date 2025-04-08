"""Projeto 02 - Gerenciador de Estoque
Criar um sistema para gerenciar um pequeno estoque de produtos. O usuário pode adicionar, remover, listar e buscar produtos.
Habilidades trabalhadas:
• Uso de dicionários para armazenar dados
• Laços (while) e condicionais (if)
• Entrada e saída de dados (input( ), print( ))"""

# Dicionário para armazenar o estoque de produtos
# A chave será o nome do produto e o valor será um dicionário com 'quantidade' e 'preco'.
estoque = {}

# Função para adicionar um produto ao estoque
def adicionar_produto():
    """
    Esta função adiciona um novo produto ao estoque ou atualiza a quantidade de um produto existente.
    A função solicita ao usuário o nome, a quantidade e o preço do produto.
    """
    nome = input("Digite o nome do produto: ").strip()  # Solicita o nome do produto, removendo espaços extras
    quantidade = int(input(f"Digite a quantidade de {nome}: ").strip())  # Solicita a quantidade do produto
    preco = float(input(f"Digite o preço de {nome}: R$ ").strip())  # Solicita o preço do produto
    
    # Verifica se o produto já está no estoque
    if nome in estoque:
        # Se o produto já existe, adiciona a nova quantidade à quantidade existente
        estoque[nome]['quantidade'] += quantidade
        print(f"Quantidade de '{nome}' atualizada para {estoque[nome]['quantidade']} unidades.")
    else:
        # Se o produto não existe, adiciona o produto com a quantidade e o preço informados
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"'{nome}' adicionado ao estoque com {quantidade} unidades, preço R$ {preco:.2f} cada.")

# Função para remover um produto do estoque
def remover_produto():
    """
    Esta função remove um produto do estoque ou diminui a quantidade do produto existente.
    O usuário pode especificar a quantidade a ser removida.
    """
    nome = input("Digite o nome do produto a ser removido: ").strip()  # Solicita o nome do produto
    
    # Verifica se o produto está no estoque
    if nome in estoque:
        quantidade = int(input(f"Digite a quantidade de {nome} a ser removida: ").strip())  # Solicita a quantidade a ser removida
        
        # Verifica se a quantidade a ser removida é maior ou igual à quantidade disponível
        if quantidade >= estoque[nome]['quantidade']:
            del estoque[nome]  # Remove o produto do estoque
            print(f"{nome} removido do estoque.")
        else:
            # Se não for para remover o produto completamente, diminui a quantidade
            estoque[nome]['quantidade'] -= quantidade
            print(f"{quantidade} unidades de {nome} removidas. Agora, restam {estoque[nome]['quantidade']} unidades.")
    else:
        # Se o produto não existir no estoque, exibe uma mensagem de erro
        print(f"{nome} não encontrado no estoque.")

# Função para listar todos os produtos no estoque
def listar_produtos():
    """
    Esta função exibe todos os produtos disponíveis no estoque com suas respectivas quantidades e preços.
    """
    if estoque:
        print("\nProdutos no estoque:")
        # Itera sobre os produtos no estoque e exibe suas informações
        for nome, info in estoque.items():
            print(f"'{nome}': {info['quantidade']} unidades, preço R$ {info['preco']:.2f}")
    else:
        # Caso o estoque esteja vazio, exibe uma mensagem
        print("O estoque está vazio.")

# Função para buscar a quantidade e preço de um produto específico no estoque
def buscar_produto():
    """
    Esta função permite buscar um produto no estoque e exibir sua quantidade e preço.
    """
    nome = input("Digite o nome do produto que deseja buscar: ").strip()  # Solicita o nome do produto
    
    # Verifica se o produto está no estoque
    if nome in estoque:
        produto = estoque[nome]
        print(f"'{nome}' tem {produto['quantidade']} unidades no estoque, preço R$ {produto['preco']:.2f}.")
    else:
        # Se o produto não for encontrado, exibe uma mensagem
        print(f"'{nome}' não encontrado no estoque.")

# Função principal que exibe o menu e chama as funções apropriadas
def menu():
    """
    Esta função exibe o menu principal e permite ao usuário escolher as opções para gerenciar o estoque.
    O menu ficará disponível até que o usuário escolha a opção de sair.
    """
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Buscar produto")
        print("5. Sair")
        
        # Solicita a escolha do usuário
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        # Chama a função correspondente à opção escolhida
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            buscar_produto()
        elif opcao == '5':
            print("Saindo do sistema...")
            break  # Sai do loop e encerra o programa
        else:
            # Se o usuário escolher uma opção inválida, exibe uma mensagem
            print("Opção inválida. Tente novamente.")

# Chama a função do menu para iniciar o programa
menu()