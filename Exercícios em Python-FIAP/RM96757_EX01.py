assinatura = input("Informe o nível de assinatura: Basic, Silver, Gold, Platinum ")
faturamento_anual = float(input("Informe o faturamento anual em R$: "))


if assinatura == "Basic":
   bonus = (faturamento_anual * 0.3)
elif assinatura == "Silver":
   bonus = (faturamento_anual * 0.2)
elif assinatura == "Gold":
   bonus = (faturamento_anual * 0.1)
elif assinatura == "Platinum":
   bonus = (faturamento_anual * 0.05)

print("O cliente deve pagar R$ {} referente ao bônus" .format(bonus))