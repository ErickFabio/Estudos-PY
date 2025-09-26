#Manipulando conjuntos - sets
#conseguimos fazer operações que faz em conjunto normalmente

usuarios = {"ana", "maria", "ana"}
usuarios.add("felipe")
print (usuarios)

usuarios_digitado = input("Digite seu usuário: ")
if usuarios_digitado in usuarios:
  print(f"Usuário cadastrado!")
else:
  print(f"Usuário não cadastrato!")

novos_usuarios = {"felipe", "pedro", "marcos"}
print(usuarios)
print(novos_usuarios)

todos_usuarios = usuarios.union(novos_usuarios)
print(f"união: {todos_usuarios}" )

usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"interceção: {usuarios_comuns}")

usuarios_diferentes = usuarios.difference(novos_usuarios)
print(f"diferença: {usuarios_diferentes}")


