#3 – Faça um programa, utilizando dicionários, peça para o usuário inserir o
#nome dos três funcionários e mostre-os na tela. Posteriormente peça para o
#usuário demitir um funcionário e mostre os funcionários restantes na tela.
# Dicionário para armazenar funcionários
funcionario= {}


nome = input('digite o nome do funcionario:')
funcionario[nome] = 'empregado'
print(funcionario)

nome = input('digite o nome do funcionario:')
funcionario[nome] = 'empregado'
print(funcionario)

nome = input('digite o nome do funcionario:')
funcionario[nome] = 'empregado'
 
print(funcionario)

demitir = input('digite o nome para ser demitido: ')
if demitir in funcionario:
 del funcionario[demitir]
 print('usuario demitido com sucesso')
else:
 print('funcionario não encontrado')

print('usuarios restantes:',funcionario)