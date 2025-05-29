#4 – Faça um programa, utilizando dicionários, que tenha as seguintes
#informações: nome, idade, cpf, endereço e rg. Peça ao usuário para digitar as
#informações. Mostre na tela primeiramente somente o dicionário, depois
#somente as chaves e depois somente os valores.
pessoa = {}

print('sua carteira esta vazia')

nome = input('nome: ')
idade = input('idade:')
cpf = input('cpf: ')
endereço = input('endereço: ')
rg = input('rg: ')

pessoa['nome'] = nome
pessoa['idade'] = idade
pessoa['cpf'] = cpf
pessoa['endereço'] = endereço
pessoa['rg'] = rg

print(pessoa)

print("Chaves do dicionário:")
for chave in pessoa:
    print(chave)


print("Valores do dicionário:")
for chave in pessoa:
    print(pessoa.get('nome'))