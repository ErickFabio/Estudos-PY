#Manipulando Dicionários  
# essa estrutura se chama: Chave"onde está nome" e Valor "onde tem o nome"

cliente = {
  "nome": "Erick", 
  "cidade": "João Pessoa", 
  "ano_nasc": 1992,
  "ativo": False
}
print(cliente["nome"]) 

cliente["ano_nasc"] = 2000
print (cliente) 

del cliente["cidade"]
print (cliente)

if "ano_nasc" in cliente:
  print(f"O Cliente nasceu em: {cliente['ano_nasc']}")
else:
  print(f"Não existe a chave ano_nasc")

  for valor, in cliente.values():
    print(valor)

  for chave, in cliente.items():
    print(chave)