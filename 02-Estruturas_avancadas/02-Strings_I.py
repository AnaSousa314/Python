#Funções de strings
# Suponhamos que temos a seguinte string:

frase = 'uma FRASE'

# Podemos acessar individualmente cada caractere em uma frase.
# A ideia é a mesma de acessar uma lista:
print(frase[0])
print(frase[1])
print(frase[2])

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")

# Porém, strings são imutáveis: não podemos alterar caracteres individuais
# A linha abaixo, se for descomentada, dará erro no programa:
# frase[4] = 'C'

# Podemos converter strings para listas:
listafrase = list(frase)
print(listafrase)

# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)

# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)

# Existem algumas funções interessantes que retornam a string "tratada":
s1 = frase.capitalize() # 1a letra maiúscula, restante minúscula
s2 = frase.title() # todo início de palavra em maiúscula, resto minúscula
s3 = frase.upper() # string inteira em maiúscula
s4 = frase.lower() # string inteira em minúscula
s5 = frase.replace('F', 'C') # substitui a primeira substring pela segunda

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
# Note que NENHUMA delas ALTERA a string original, elas sempre retornam
# a string nova.
print('String original:', frase)

# Outra possibilidade com strings é quebrar a string em uma lista de substrings
# Sempre que o caractere especificado é encontrado, a string é quebrada
quebra1 = frase.split(' ') # quebra a frase no caractere espaço em branco
quebra2 = s3.split('A') # quebra a frase em maiúsculas no caractere 'A'

print(quebra1)
print(quebra2)

# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)
# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)
# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'


# Como fazer para se colocar aspas duplas dentro de uma frase. Usa-se a contrabarra antes de cada aspa.
frase2 = "O professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\"."
print(frase)

# Também podemos usar o slice em strings
# Muito parecido com uma Tupla
empresa = 'Google'  
print(empresa[:3])

# Usamos o split para quebrar uma string a partir de um caracter, ou mesmo espaço
nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

# O strip serve para retirar espaço excessivos de uma string
cabecalho = '        Menu Principal    '
print(cabecalho)
# Retira espaços excessivos
print(cabecalho.strip())

##
nome_cidade = 'rio DE janeiro'
# Esses métodos são muito usados para ser possível comparar strings
print(nome_cidade.title()) # formatacao de titulo, cada palavra comeca com letra maiuscula
print(nome_cidade.capitalize()) # primeira letra da frase em maiuscula, resto em minuscula
print(nome_cidade.lower()) # tudo minusculo
print(nome_cidade.upper()) # tudo maiusculo

# Exemplo de para que serve os métodos de string
nome_city = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')
nome_city = nome_city.strip()
while nome_city.lower() != 'rio de janeiro':
    print('Tenta de novo.')
    nome_city = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')

print('Booaa!')


# Operador in em string também serve para encontararmos algo nela
menssagem = 'Você viu o que o Pietro disse na sala ontem?'
fui_citado = 'Pietro' in menssagem
print(fui_citado)