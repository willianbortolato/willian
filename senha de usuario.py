# captação de input de usuario
senha =str(input("digite sua senha de entrada"))
if (senha == "admin"):
    print("ola adminitrador")
elif (senha == "user"):
    print("ola usuario")
else:
    print("acesso negado. Verifique sua senha")

