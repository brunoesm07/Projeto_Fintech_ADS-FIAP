valor_bruto = float(input("Insira o valor do pacote: "))
categoria = input("Escolha a categoria dos assentos: Economica, Executiva, Primeira Classe ")
quantviajantes = int(input("Insira a quantidade de viajantes: "))

if categoria == "Economica" and quantviajantes == 2:
    valor_liquido = valor_bruto * 0.97
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 3%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}" .format(valor_medio))
elif categoria == "Economica" and quantviajantes == 3:
    valor_liquido = valor_bruto * 0.96
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 4%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}".format(valor_medio))
elif categoria == "Economica" and quantviajantes >= 4:
    valor_liquido = valor_bruto * 0.95
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 5%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}".format(valor_medio))

if categoria == "Executiva" and quantviajantes == 2:
    valor_liquido = valor_bruto * 0.95
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 5%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}" .format(valor_medio))
elif categoria == "Executiva" and quantviajantes == 3:
    valor_liquido = valor_bruto * 0.93
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 7%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}".format(valor_medio))
elif categoria == "Executiva" and quantviajantes >= 4:
    valor_liquido = valor_bruto * 0.92
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 8%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}".format(valor_medio))

if categoria == "Primeira Classe" and quantviajantes == 2:
    valor_liquido = valor_bruto * 0.90
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 10%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}" .format(valor_medio))
elif categoria == "Primeira Classe" and quantviajantes == 3:
    valor_liquido = valor_bruto * 0.85
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 15%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}".format(valor_medio))
elif categoria == "Primeira Classe" and quantviajantes >= 4:
    valor_liquido = valor_bruto * 0.80
    valor_medio = valor_liquido / quantviajantes
    print("Valor do pacote: R$ {}" .format(valor_bruto))
    print("Desconto de 20%")
    print("Valor a pagar: R$ {}" .format(valor_liquido))
    print("O valor médio por passageiro é de R$ {}".format(valor_medio))

else:
    print("Valor do pacote: R$ {}".format(valor_bruto))
    print("Sem direito a desconto")