valores = [100, 30, 45, 33, 99]

def mensagem():
  print("Olá Mundo!")

def calcular_desconto(preco):
  preco_final = preco * 0.8
  return preco_final

def soma(a, b):
  return a + b

mensagem()
valor_pagar = calcular_desconto(100)
print(f"{valor_pagar:.2f}") #caso queira usar casa decimal a mais, colocar em string, valor+f

total = soma(4, 90)
print(total)

print("### Valores com Desconto ###") 
for valor in valores:
  valor_desconto = calcular_desconto(valor)
  print(f"{valor_desconto:.2f}")