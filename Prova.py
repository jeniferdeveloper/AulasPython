import numpy as np
""" 1. Você tem a lista dados = [10, 20, 30].
Qual comando converte essa lista para tupla?

list(dados)
dados.tuple()
to_tuple(dados)
tuple(dados) CORRETA"""

""" 2. Dado um array,  qual comando retorna a média?

np.median(a)
a.mean()
np.average(a)
np.mean(a) CORRETA

a = np.array([10,20,30,40])
print("Média: ", np.mean(a))"""

"""3. Você está trabalhando com uma lista de números inteiros que representa os pontos de um jogador em cada fase de um jogo:
#Qual comando exibe corretamente o terceiro valor da lista? 

pontos = [100,200,150,300,250]
print(pontos[2])

print(pontos[2]) CORRETA
print(pontos[3])
print(pontos[1])
print(pontos[4])

#pontos[0] → 100 (primeiro elemento)
#pontos[1] → 200 (segundo elemento)
#pontos[2] → 150 (terceiro elemento)
#pontos[3] → 300 (quarto elemento)
#pontos[4] → 250 (quinto elemento)"""

#4. Qual comando imprime todas as notas da Ana? 
#notas = {'Ana': [7,8], 'Joao': [5,6]}
#print(notas.Ana)
#print(notas['Ana']) # CORRETA
#notas['Joao']
#print(notas.get('Joao'))

"""# 5. Qual valor é retornado por matriz[2][0]? 
matriz = [[1,2], [3,4], [5,6]]
print(matriz[2][0])
6
3
2
5 CORRETA """

""" 6. Qual das opções abaixo representa uma tupla de um único elemento?  
(5)
5,
[5]
(5,)

tupla_correta = (5,)
print(type(tupla_correta))"""

"""7.Qual das opções abaixo representa uma tupla de um único elemento?  

(5)
5,
[5]
(5,) CORRRETA"""

#8. Qual trecho de código abaixo conta corretamente quantos números pares há entre 1 e 10?  
"""cont = 0
for i in range(1,11):
    if i % 2 == 0:
    cont += 1

        for i in range(1,11):
        if i % 2 == 0:
            cont += 1

        print(cont) OPÇÃO CORRETA

cont = 0
for i in range(1,10):
    if i % 2 != 0:
    cont += 1

cont = 0
for i in range(2,11,2):
    cont = cont + 2

for i in range(1,11):
    if i % 2 == 0:
        print(i) (CORRETA) ERRADA A PERGUNTA PEDE APENAS PARA CONTAR O RESULTADO SERÁ 5"""

# 9. Considere a lista abaixo.
#Após efetuar os comandos, qual será o conteúdo final da lista dados?

#[1, 2, 3]
#[2, 3, 4] CORRETA
#[4, 2, 3]
#[1, 2, 4]

#dados = [1,2,3]
#dados.append(4) #Adiciona o número 4 ao final da lista, resultando em [1, 2, 3, 4].
#dados.pop(0) # Remove o primeiro elemento (índice 0), que é o 1, resultando em [2, 3, 4].
#print(dados)

#10.Você deseja criar uma matriz 5x5 preenchida com zeros. Qual comando é o correto?  
#matriz = [0]*5

#matriz = np.zeros((5,5)) CORRETA
#print(matriz)

#matriz = np.ones(5,5)
#matriz = [ [0,0,0,0,0] ]

"""11. Dado o código abaixo, qual será a saída?

[1, 2, 3, 1, 2, 3]
[2, 4, 6] CORRETA
[1, 4, 9]
[1 2 3 1 2 3]
vetor = np.array([1,2,3])
print('Vetor: ', vetor * 2)"""

#12. Você declarou a tupla abaixo.  
#Qual das opções abaixo causaria erro de execução?  
#cores = ('azul', 'verde', 'vermelho')
#print(cores[1]) OK Acessa o elemento no índice 1 ('verde')
#print(len(cores)) OK Retorna o tamanho da tupla (3). 
#cores[0] = 'amarelo' ERRADO Tuplas são imutáveis, ou seja, não podem ter seus elementos alterados após a criação
#print(cores)
#print('verde' in cores) Verifica se 'verde' está na tupla (True).

"""13. Qual comando cria uma matriz 3x3 com números entre 1 e 100?  
np.zeros((3,3))
np.random.randint(1, 101, (3,3)) CORRETA
np.random((3,3), 1, 100)
np.array([1:100])

matriz = np.random.randint(1, 101, (3,3))
print(matriz)"""

#14.Considere o dicionário abaixo.
#Qual comando retorna o preço da maçã?  
#precos.maçã
#precos[1]
#precos['maçã'] CORRETA
#precos(maçã)

#precos = {'banana': 2.5, 'maçã': 3.0, 'uva': 4.0}
#print(precos['maçã'])

"""15. Qual é o resultado de arr * arr?  
arr = np.array([1,2,3])
[2, 4, 6]
[1, 4, 9] CORRETA
[1, 2, 3, 1, 2, 3]
[0, 0, 0]

arr = np.array([1,2,3])
print(arr*arr)"""

"""16.Qual código verifica corretamente se um número digitado é positivo?  

if numero = 0:
if numero > 0: CORRETO
if numero => 0:
if numero < 0:"""

"""17. Qual é uma vantagem do np.array() sobre listas nativas do Python?  

Suporte a strings
Armazenamento de múltiplos tipos
Operações matemáticas vetoriais otimizadas CORRRTA
Ordenação por padrão"""

""""18. Qual trecho permite que o usuário digite nomes de alunos até decidir parar?

for nome in nomes:
    print(nome)

for input('nome') != '':
    break

while True:
    nome = input('Digite:')
    if nome == 'n':
        break CORRETA

while nome != 'n':
    input('Digite: ')"""

""" 19.Dado o trecho abaixo, o que esse código verifica?

Se o nome contém números
Se o nome tem mais de uma letra
Se o nome contém apenas letras CORRETA
Se o nome está em minúsculo

import re 
nome = input('Digite seu nome: ')
if re.match('^[A-Za-z]+$', nome):
    print('Nome valido')
else:
    print('Nome invalido')"""

"""20. Você recebeu a lista numeros = [1, 2, 3, 4, 5, 6]. Deseja somar apenas os pares.

Qual é o resultado correto da operação?

12 CORRETA
10
9
11"""

"""21.Qual das opções imprime todas as chaves e valores de um dicionário chamado agenda?  

for chave in agenda:
for chave, valor in agenda.items(): print(chave, valor) CORRETA
for valor in agenda:
agenda.each()"""

cont = 0

"""for i in range(1,11):
    if i % 2 == 0:
        print(i) """


