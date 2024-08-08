#criar uma lista com 5 frutas
frutas = ['morango', 'maça', 'laranja', 'kiwi', 'uva']
print(frutas)

#crie uma lista com 10 numeros e emprima o primeiro e o ultimo numero
numero = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
print(numero[0])
print(numero[9])

#criar uma lista com os numeros 5 10 e 15 e remover o 10
numeros = []
numeros.insert(0,'5')
numeros.insert(1,'10')
numeros.insert(2,'15')
print(numeros)
numeros.remove('10')
print(numeros)

#criar uma lista com os dias da semana e emprimir o numero de elementos
dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
print(dias)
print(len(dias))

#crie uma lista com 5 paises e verifique se o brasil esta nela, imprima a lista informando
paises = ['colombia', 'venezuela', 'paraguai', 'peru', 'equador']
print(paises)
print('brasil' in paises)
