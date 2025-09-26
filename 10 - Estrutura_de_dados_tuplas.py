#Manipulando tuplas - tuple

cores = ("vermelho", "azul", "amarelo", "verde", "azul")
print(f"Meu carro é {cores[2]}")
      
qtd = len(cores)
print(f"Tenho {qtd} de opções de cores")

cor = input("Digite uma cor: ")
if cor in cores: #serve para listas,tuplas ou qualquer outra estrutura de dados
  qtd_cor = cores.count(cor)
  print (f"Temos {qtd_cor} tipo de {cor}")
else:
  print (f"A cor {cor} não existe na Loja")

aluno = ("Erick", 10, 5)
nome, nota1, nota2 = aluno 
media = (nota1 + nota2) / 2
print (f"O Aluno {nome} com as notas {nota1} e {nota2} está com a média {media}")