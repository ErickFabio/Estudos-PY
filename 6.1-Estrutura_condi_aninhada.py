nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequência: "))

if nota >= 5 and frequencia >= 75:
  situacao = "Aprovado"
elif nota >= 5 or frequencia >= 75:
  situacao = "Recuperação"
else:
  situacao = "Reprovado"

print (f"Você está {situacao}!")