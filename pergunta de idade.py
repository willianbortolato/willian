# declarando variável
idade = float(input("digite sua idade"))
#deixar linha em branco
print()
if idade < 12:
    print('criança', idade)
elif idade < 18:
    print('adolecente',idade)
elif idade <60:
    print('adulto', idade)
else:
    print('idoso')

