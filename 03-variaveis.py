# - Variaveis e tipos de dados -

# 1 - O que é uma varíavél?
# É um espaço reservado na memória, que serve para armazenar qualquer tipo de dado. 

#2 - O que é tipagem dinâmica? 
# Siginifica que não é necessário expecificar, na declaração o tipo de variável 

#ex de nome de variável (snake Case): 
nome_aluno = "Fernando"
nota_aluno = 8

print(nome_aluno)
print(nota_aluno)

#3 - Quais os tipos de dados em phyton?
# Inteiro (int), decimal (float), complexo (comples), 
# string (str), boolean (bool), list, 
# Exemplos:
ano_atual = 2023
desconto = 15.59
cidade = "João Pessoa"
filhos = False
Cores = ["branco", "azul", "verde"]
frutas = ("banana", "uva")
notas = {5,10,15}
Clientes = {
  "nome": "Maria",
  "altura": 1.95,
  "peso": 60.00
}

#4 - O que é tipagem forte?
numero1 = 23
numero2 = "100"
print (numero1 + numero2)


#5 - Como trocar o tipo de váriavél?
preco_produto = 1.90
preco_produto = str(preco_produto)
preco_produto = float(preco_produto)

print (type (preco_produto))