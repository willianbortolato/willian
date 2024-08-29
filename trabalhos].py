contador = 0
while contador < 10:
    contador +=1
    print(contador)


print()
print()
print()


a = 0
print(a)
while a < 20:
    a += 2
    print(a)


print()
print()
print()


senha_correta = '05072022'
tentativa = input('digite a senha:')

while tentativa != senha_correta:
    print('senha incorreta. tente novamente')
    tentativa = input('digite a senha:')
    if tentativa !=senha_correta:
        print('senha incorreta. tente novamente')
    tentativa = input('digite a senha:')
    if tentativa !=senha_correta:
        print('bloqueado por muitas tentativas sem acerto')
        print('tente novamente mais tarde')
        break
else:
    print('senha correta, acesso concedido')