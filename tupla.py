#capitulo tuplas
#primeira tupla
tupla1 = ('gato', 'cachorro', 'papagaio', 'tartaruga')
print(tupla1)

#acessando um elemento da tupla
print(tupla1[2])

#slicing de uma tupla
print(tupla1[1:3])

# criando lista vazia
tupla_vazia = ()
print(tupla_vazia)

#erro de tupla
#tupla1[1] = 'elefante'

#apagar tupla, use del()
#del(tupla1)
#print(tupla1)







#trabalhar com tupla
tupla2 = (8.3, 9.4, 3.3, 7.5, 7.6)
print(max(tupla2))
print(min(tupla2))
print(len(tupla2))

#transformando uma tupla em lista e vice versa
lista1 = list(tupla1)
print(lista1)
lista2 = ['José', 'afonso', 'carlos', 'luiz']
tupla3 = tuple(lista2)
print(tupla3)