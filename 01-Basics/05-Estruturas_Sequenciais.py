""" Outputs
Chamamos de saídas ou outputs do nosso programa todos os dados que são gerados pelo programa e fornecidos para o usuário.

Já conhecemos a função print() que recebe um valor ou uma sequência de valores e realiza a tarefa de imprimí-los na tela.

y = 3.14 # uma variável do tipo real (float)
escola = "Let's Code" # uma variável literal (string)

# Podemos exibir textos na tela e/ou valores de variáveis com a função print().
print('eu estudo na ', escola)
print('pi vale', y)

# Podemos fazer operações dentro do print:
print (y+1, y**2)
Inputs
Já as entradas ou inputs do nosso programa são as informações que o usuário possui e deve fornecer ao código.

# Podemos ler valores do teclado com a função input().
# Ela permite que a gente passe uma mensagem para o usuário.
nome = input('Digite o seu nome: ')

# Tudo que é lido por input() é considerado uma string (str).
# Para tratar como outros tipos de dados é necessário realizar a conversão:
peso = float(input('Digite o seu peso: ')) # lê o peso como número real
idade = int(input('Digite a sua idade: ')) # lê a idade como número inteiro

print(nome, 'pesa', peso, 'kg e tem', idade, 'anos de idade.') """


#É executado linha a linha
#todo valor lido pelo input sempre sera string, precisamos fazer a conversao

print(float('123456'))
print(str(123456))
print(bool(''))
print(bool('abc'))#Retorna True
print(bool(0))#apenas o zero é mapeado como falso, todos os outros valores são mapeados como True
print((bool(-2)))