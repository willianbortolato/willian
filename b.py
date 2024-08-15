#tupla de frutas
tupla1 = ('maçã', 'banana', 'morango', 'kiwi', 'maracujá')
print(tupla1)
print()
#tupla de 1 a 10, imprimir primeiro terceiro e ultimo
tupla2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla2[0])
print(tupla2[2])
print(tupla2[9])
print()

#concatenar tupla
tupla1 = ('maçã', 'banana', 'morango', 'kiwi', 'maracujá')
tupla3 = ('amarelo', 'azul', 'roxo', 'preto', 'verde')
tupla4 = (tupla1 + tupla3)
print(tupla4)

print()
#tupla de semana
tuplasemana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
print(len(tuplasemana))

print()
#verificar
tuplapaises = ('brazil', 'alemanha', 'italia', 'belgica', 'australia')
print('brazil'in(tuplapaises))