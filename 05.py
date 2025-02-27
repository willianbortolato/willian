numero1 = float(input("digite o primeiro numero"))
numero2 = float(input("digite o segundo numero"))
operação = input("digite uma operação(+, -, *, /):")
if operação == '+':
    print(numero1 + numero2)
elif operação == '-':
    print(numero1 - numero2)
elif operação == '*':
    print(numero1 * numero2)
elif operação == '/':
    print(numero1 / numero2)
else:
    print("operação inválida")