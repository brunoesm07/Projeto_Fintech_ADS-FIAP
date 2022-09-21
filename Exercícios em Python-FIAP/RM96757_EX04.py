minutos = int(input("Informe os minutos atuais "))

fatorial = 1
i = 1

while minutos >= i:
    fatorial *= i
    i += 1

print("A senha é LIBERDADE{}" .format(fatorial))