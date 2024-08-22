numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 7 in numeros:
    numeros.remove(7)
else:
    numeros.append(7)
print('o 7 foi removido')
print()
print()
print()
lista = ['maçã', 'banana', 'laranja']
if 'uva' in lista:
   print(lista)
else:
    lista.append('uva')
print(lista)
print()
print()
print()
numero = [55, 2, 3, 4]
if numero[0] % 2 == 0:
    index = numero.index(numero[0])
    numero[index] = numero[0]*2
else:
    index = numero.index(numero[0])
    numero[index] = numero[0] / 2
print(numero)