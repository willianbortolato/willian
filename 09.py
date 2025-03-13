nota = int(input("Digite a nota (0-100): "))

if 90 <= nota <= 100:
    classificacao = "A"
elif 80 <= nota <= 89:
    classificacao = "B"
elif 70 <= nota <= 79:
    classificacao = "C"
elif 60 <= nota <= 69:
    classificacao = "D"
elif 0 <= nota <= 59:
    classificacao = "F"
else:
    classificacao = "Nota inválida"

print(f"Classificação: {classificacao}")