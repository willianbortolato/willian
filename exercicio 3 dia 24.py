def armazenar_e_mostrar_valores_simplificado():
  valores = []
  while True:
    entrada = input("Digite um valor (ou 'fim' para terminar): ")
    if entrada.lower() == 'fim':
      break
    valores.append(entrada)

  print("Valores armazenados:")
  print(valores) # Imprime a lista diretamente

armazenar_e_mostrar_valores_simplificado()
