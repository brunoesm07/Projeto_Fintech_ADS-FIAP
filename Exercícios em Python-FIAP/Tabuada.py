# Tabuada usando while
n = int(input("Qual o número que você deseja saber a tabuada? "))
i = 1
# i é a nomenclatura padrão para contador

while i <= 10:
    print("{} x {} = {} ".format(n, i, n * i))
    i = i + 1

# Loop até 9
for x in range(10):
    print(x)

# Loop de 2 até 9
for x in range(2, 10):
    print(x)

# Loop de 2 até 90 pulando 2
for x in range(2, 100, 2):
    print(x)

# Tabuada usando for
n = int(input("Qual o número que você deseja saber a tabuada? "))
for i in range(1, 11):
    print("{} x {} = {} ".format(n, i, n * i))