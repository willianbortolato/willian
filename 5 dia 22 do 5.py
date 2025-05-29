#5 – Faça um programa, utilizando dicionários, que cadastre todos os
#integrantes de uma família. Cada integrante tem as seguintes informações:
#nome, idade, endereço e grau de parentesco. Para resolver esse exercício crie
#um dicionário aninhado. Mostre todo o dicionário na tela e peça para o usuário
#uma informação específica que queira de algum integrante. Siga as seguintes
#orientações: deve possuir um dicionário família, dentro desse dicionário deve
#ter o nome dos integrantes (cada nome também será um dicionário).
familia = {}

num_integrantes = int(input("Quantos integrantes tem a família? "))
for _ in range(num_integrantes):
    nome = input("Digite o nome do integrante: ")
    familia[nome] = {
        'idade': input("Digite a idade: "),
        'endereço': input("Digite o endereço: "),
        'grau_parentesco': input("Digite o grau de parentesco: ")
    }

print("Dicionário família completo:",familia)


# Consulta específica
integrante = input("Digite o nome do integrante que deseja consultar: ")
if integrante in familia:
    print("Informações disponíveis: idade, endereço, grau_parentesco")
    info = input("Qual informação deseja? ")
    if info in familia[integrante]:
        print(integrante + ": " + info + " = " + familia[integrante][info])
    else:
        print("Informação não encontrada.")
else:
    print("Integrante não encontrado.")
