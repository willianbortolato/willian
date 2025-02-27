idade = int(input("escreva a sua idade"))
if idade <= 12:
    print("é criança")
elif idade == 13:
    print("é adolescente")
elif idade <= 17:
    print("é adolescente")
elif idade == 18:
    print("é adulto")
elif idade <= 59:
    print("é adulto")
else:
    print("é idoso")