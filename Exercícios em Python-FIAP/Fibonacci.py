numero_imput = int(input("Insira um número inteiro "))

anterior1 = 0
anterior2 = 1

for n in range (1, numero_imput + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_imput == atual:
        print("Ação bem sucedida!")
        break
    elif numero_imput < atual:
        print("Ação falhou")
        break