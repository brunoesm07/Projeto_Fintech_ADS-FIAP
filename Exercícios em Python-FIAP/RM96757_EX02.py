print("Olá, por favor informe a quantidade de votos em cada dia da semana.")
segunda = int(input("Quantos votos na segunda-feira? "))
terca = int(input("Quantos votos na terça-feira? "))
quarta = int(input("Quantos votos na quarta-feira? "))
quinta = int(input("Quantos votos na quinta-feira? "))
sexta = int(input("Quantos votos na sexta-feira? "))



if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido foi segunda-feira.")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia escolhido foi terça-feira.")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia escolhido foi quarta-feira")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia escolhido foi quinta-feira")
else:
    print("O dia escolhido foi sexta-feira")

