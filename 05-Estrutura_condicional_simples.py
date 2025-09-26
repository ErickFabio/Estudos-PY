horas_trabalhadas = float(input ("Digita a quantidade de horas trabalhadas: "))
valor_hora = float(input ("Digita o valor/hora: "))

if (horas_trabalhadas >=100):
   bonus = 500,00
else:
   bonus = 0

salario = horas_trabalhadas * valor_hora

Salario =horas_trabalhadas * valor_hora + bonus

print (f"seu salario é de {salario}")