while True:
    print("Escolha uma atividade para executar:")
    print("1 - Adicionar elementos a um dicionário vazio")
    print("2 - Cadastrar 3 produtos de mercado e seus preços")
    print("3 - Cadastrar funcionários e demitir um")
    print("4 - Cadastrar informações pessoais e exibir chaves/valores")
    print("5 - Cadastrar integrantes de uma família (dicionário aninhado)")
    print("0 - Sair")

    opção_user = input("Digite o número da opção desejada: ")

    if opção_user == '1':
        dicionario = {}
        while True:
            opcao = input('Gostaria de criar alguma chave? (sim/não): ').lower()
            if opcao == "não":
                break
            elif opcao == "sim":
                chaves = input('Digite uma chave para ser criada dentro do dicionário: ')
                valores = input('Digite um valor para ser colocado dentro da chave: ')
                dicionario[chaves] = valores
            else:
                print("Opção inválida. Por favor, digite 'sim' ou 'não'.")
        print("Dicionário final:", dicionario)

    elif opção_user == '2':
        dicionario = {}
        for i in range(3):
            produto = input(f'Digite o nome do produto {i}: ')
            valor = float(input(f'Digite o valor do produto {produto}: '))
            dicionario[produto] = valor
            print(dicionario)

    elif opção_user == '3':
        funcionario = {}
        for i in range(1, 4):
            nome = input(f'Digite o nome do funcionário {i}: ')
            funcionario[nome] = 'empregado'
            print(funcionario)

        demitir = input('Digite o nome do funcionário para ser demitido: ')
        if demitir in funcionario:
            del funcionario[demitir]
            print('Usuário demitido com sucesso.')
        else:
            print('Funcionário não encontrado.')
        print('Funcionários restantes:', funcionario)

    elif opção_user == '4':
        pessoa = {}
        print('Sua carteira está vazia')

        nome = input('Nome: ')
        idade = input('Idade: ')
        cpf = input('CPF: ')
        endereco = input('Endereço: ')
        rg = input('RG: ')

        pessoa['nome'] = nome
        pessoa['idade'] = idade
        pessoa['cpf'] = cpf
        pessoa['endereço'] = endereco
        pessoa['rg'] = rg

        print("Dicionário completo:", pessoa)

        print("Chaves do dicionário:")
        for chave in pessoa:
            print(chave)

        print("Valores do dicionário:")
        for chave in pessoa:
            print(pessoa[chave])

    elif opção_user == '5':
        familia = {}
        num_integrantes = int(input("Quantos integrantes tem a família? "))
        for _ in range(num_integrantes):
            nome = input("Digite o nome do integrante: ")
            familia[nome] = {
                'idade': input("Digite a idade: "),
                'endereço': input("Digite o endereço: "),
                'grau_parentesco': input("Digite o grau de parentesco: ")
            }

        print("Dicionário família completo:", familia)

        integrante = input("Digite o nome do integrante que deseja consultar: ")
        if integrante in familia:
            print("Informações disponíveis: idade, endereço, grau_parentesco")
            info = input("Qual informação deseja? ")
            if info in familia[integrante]:
                print(f"{integrante}: {info} = {familia[integrante][info]}")
            else:
                print("Informação não encontrada.")
        else:
            print("Integrante não encontrado.")

    elif opção_user == '0':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, digite um número de 0 a 5.")