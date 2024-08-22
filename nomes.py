dados = {'produto': 'camisa','preço': 20, 'desconto': 20}
if 'desconto' in dados:
    dados['desconto'] = 40
    print(dados)
else:
    dados['desconto']=+40
print(dados)