numeros = (10,20, 30, 40, 50)
if 30 in numeros:
    print('numero encontrado')
else:
    print('numero não encontrado')

print()
print()
print()
tupla_100 = (1, 2, 3, 4, 100)
if 100 in tupla_100:
    print('100 está na tupla')
else:
    print('100 não está na tupla')
print()
print()
print()
tupla_nomes = ('Ana, Willian, Michael')
if 'Ana' in tupla_nomes:
    print('ana está na tupla')
else:
    print('ana não esta na tupla')
print()
print()
print()
def substituir_por_dobro_ou_metade(numero):
    if numero % 2 == 0:  # Verifica se o número é par
        return numero * 2  # Substitui por seu dobro
    else:
        return numero / 2  # Substitui por sua metade
