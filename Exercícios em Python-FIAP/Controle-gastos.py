transacoes = int(input("Informe a quantidade de transações financeiras no dia: "))
i = 0
valor_gasto = 0

while i <= transacoes - 1:
    valor_gasto = valor_gasto + float(input("insira o valor gasto: "))
    i = i + 1

valor_medio = (valor_gasto / i)

print("O valor total gasto foi de R$ {} com um gasto médio de R$ {:.2f} ".format(valor_gasto, valor_medio))
