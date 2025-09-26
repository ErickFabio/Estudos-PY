#Manipulando listas - list

nomes = ["Ana","Pedro"]
print (f"Lista Original: {nomes}")

for con in range(1):
    novo_nome = input("Digite um nome{cont}:")
    nomes.append(novo_nome)
print(f"lista adicionando 2 nomes: {nomes}")

resp = "s"
while resp == "s":
    novo_nome = input(f"Digite um nome: ")
    nomes.append(novo_nome)
    resp = input ("Deseja cadastra mais um nome[s/n]: ")

print(f"lista adicionando n nomes: {nomes}")

#Listando elementos pela posição.
print(nomes[0]) 

# Removendo o último elemento da lista
nomes.pop()
print(f"Removendo o último: {nomes}")

#Remolvendo um Elemento qualquer
nomes.remove("Pedro")
print (f"Removendo um elemento: {nomes}")

#Verificando a Existência de um elemento
nome_pesquisado = input ("Digite um nome para pesquisar: ")
if nome_pesquisado in nomes:
    print("Nome Cadastrado")
else:
    print("Nome não cadastrado")

