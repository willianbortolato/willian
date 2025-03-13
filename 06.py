ld1 = float(input("Digite o comprimento do primeiro lado: "))
ld2 = float(input("Digite o comprimento do segundo lado: "))
ld3 = float(input("Digite o comprimento do terceiro lado: "))

if ld1 + ld2 > ld3 and ld1 + ld3 > ld2 and ld2 + ld3 > ld1:
    if ld1 == ld2 == ld3:
        print("Triângulo equilátero")
    elif ld1 == ld2 or ld1 == ld3 or ld2 == ld3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo válido")