#2 – Faça um código que receba dois números inteiros, utilize as quatro
#operações básicas pra gerar resultados com esses dois números e mostre os
#resultados. Cada operação deve utilizar uma função.
num1 = int(input('digite um numero inteiro:'))
num2 = int(input('digite um numero inteiro:'))

def soma(num1,num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    return num1 / num2

total = 0

while True:
    operação = input("digite 'soma', 'subtrair', 'multiplicar', 'dividir' ou 'sair': ").lower()
    if operação == 'sair':
        break
    elif operação in ['somar', 'subtrair', 'multiplicar', 'dividir']:
        valor = float(input('digite o valor:'))
        if operação == 'somar':
            total = soma(num1, num2)

        elif: opração ==
        else:
            total = subtrair(num1, num2)
    else:
        print('operação invalida')

print(f'total final: resultado{total:.2f}')