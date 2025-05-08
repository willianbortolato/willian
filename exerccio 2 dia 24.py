
def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Erro! Divisão por zero não é pode."
    return num1 / num2

total = 0

while True:

    operacao = input("Digite 'soma', 'subtrair', 'multiplicar', 'dividir' ou 'sair': ").lower()

    if operacao == 'sair':
        break
    elif operacao in ['soma', 'subtrair', 'multiplicar', 'dividir']:
        num1 = int(input('Digite o primeiro número inteiro: '))
        num2 = int(input('Digite o segundo número inteiro: '))
        if operacao == 'soma':
            total = soma(num1, num2)
        elif operacao == 'subtrair':
            total = subtrair(num1, num2)
        elif operacao == 'multiplicar':
            total = multiplicar(num1, num2)
        elif operacao == 'dividir':
            total = dividir(num1, num2)
        print(f'Resultado da {operacao}: {total}')
    else:
        print('Operação inválida')

print('Fim das operações.')
