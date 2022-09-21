aluno = 1
nota_impar = 0

for aluno in range(1, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    nova_nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} " .format(aluno)))
    nota_impar = nota_impar + nova_nota
    media_impar = (nota_impar / 25)

print("A média da metade ímpar é {}" .format(media_impar))

aluno = 2
nota_par = 0

for aluno in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nova_nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {} " .format(aluno)))
    nota_par = nota_par + nova_nota
    media_par = (nota_par / 25)

print("A média da metade par é {}" .format(media_par))

if media_impar > media_par:
    print("A média mais alta foi da turma ímpar.")
else:
    print("A média mais alta foi da turma par.")