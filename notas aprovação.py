nota = float(input("digite sua nota"))
#deixar linha em branco
print()
if nota < 5:
    print('reprovado',)
elif nota > 7:
    print('aprovado',)
else:
    print('recuperação')