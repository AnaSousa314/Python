""" 
Listas
Listas são coleções de objetos em Python. Ao invés de declarar 1 variável para cada valor que gostaríamos de armazenar, podemos criar uma lista para armazenar vários valores.

# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)

# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(numeros[indice])
    indice = indice + 1
Funções de listas
Algumas funções podem nos ajudar a trabalhar com listas. Ao percorrermos nossa lista com um while, poderíamos usar len() caso não soubéssemos o comprimento da lista.

indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1
Outra função útil é lista.append(), que coloca um elemento novo ao final da lista.

animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta == 's' or resposta == 'S'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)
A função lista.remove() deleta um elemento da lista. (mas dá erro se o elemento não existir).

animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)
Algumas outras funções úteis:

lista.count() conta quantas vezes um elemento aparece.
jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)
lista.index() busca em um elemento e fala em qual posição ele aparece.
rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)
lista.sort() ordena uma lista.
jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)
As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor.
digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)
Tuplas
# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)

# Podemos declarar sem parênteses também:
numeros = 1,2,3,5,7,11

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

'''
Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)

# Também pode-se usar o unpacking com uma tupla:
a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)
"""

# Declarando uma lista
nomes_paises = ['Brasil','Argentina','China','Canadá']
print(nomes_paises)

# Vendo o Tamanho da Lista
print('Tamanho da lista',len(nomes_paises))

# Imprimindo um item especifico da lista pelo seu index
print('País',nomes_paises[3])

# Imprimindo um item especifico da lista pelo seu index negativo, ou seja, a partir do ultimo elemento
print('País',nomes_paises[-1])

# Atribuindo um novo valor para um item da lista atraves do seu index
nomes_paises[3] = 'Colombia'
print('País',nomes_paises[3])
print(nomes_paises)

# Usando o slice para imprimir uma quntidade especifica dos items da lista
# sendo [primeiroEscolhido : segundoEscolhido]
print(nomes_paises[0:2])

# ou
print(nomes_paises[1:-1])

# do primeiro escolhido ao ultimo elemento da lista
print(nomes_paises[2:])

# do primeiro item da lista ao segundo escolhido
print(nomes_paises[:2])

# imprimindo todos os elementos com o slice
print(nomes_paises[:])

# Colocando um step para especificar de quantos em quantos será impresso. No caso de 2 em 2 a partir do primeiro item da lista
print(nomes_paises[::2])

# Verificando se existe um elemento especifico na lista atraves do 'in', que retorna True ou False
print("Brasil" in nomes_paises)

# Verificando se NÃO existe um elemento especifico na lista atraves do 'in', que retorna True ou False
print("Colombia" not in nomes_paises)

# Atribuindo novos valores a uma lista
lista_capitais = [] 
lista_capitais.append('Brasília')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogota')

print(lista_capitais)

# Inserindo um novo valor na lista em um indice especifico. Note que ele não exclui o elemento que ja estava presente nesse index
lista_capitais.insert(2,'Paris')
print(lista_capitais)

# Removendo um elemento especifico da lista 
lista_capitais.remove('Buenos Aires')
print(lista_capitais)

# Removendo um item da lista atraves de seu index e devolvendo ele 
removido = lista_capitais.pop(2)
print(lista_capitais,removido)

# Declarando uma Tupla de duas formas diferentes. Tuplas são imutáveis depois de declaradas
nomes_paises = ('Brasil','Argentina','China','Canada','Japao')
print(nomes_paises)

nomes_paises = 'Brasil','Argentina','China','Canada','Japao','Brasil'
print(nomes_paises, type(nomes_paises))

# Declarando uma Tupla de elemento unico
nome_estado = 'São Paulo',
print(nome_estado,type(nome_estado))

# Fazendo um unpacking da tupla. Note que isso não é possível em uma Lista
b,a,c,ca,j,br = nomes_paises

# imprindo os valores do unpacking
print(b,c,j)

# imprimindo os elementos da tupla separadamente
print(*nomes_paises)