num = 0
while num >= 0:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    if num < 2:
        print(f"{num} não é primo.")
    else:
        divisor = 2
        while divisor < num:
            if num % divisor == 0:
                print(f"{num} não é primo.")
                break
            divisor += 1
        else:
            print(f"{num} é primo.")