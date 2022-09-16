voto1 = int(input("Digite seu voto: 1 - Playstatio, 2 - XBOX, 3 - Nintendo "))
voto2 = int(input("Digite seu voto: 1 - Playstatio, 2 - XBOX, 3 - Nintendo "))
voto3 = int(input("Digite seu voto: 1 - Playstatio, 2 - XBOX, 3 - Nintendo "))
voto4 = int(input("Digite seu voto: 1 - Playstatio, 2 - XBOX, 3 - Nintendo "))
voto5 = int(input("Digite seu voto: 1 - Playstatio, 2 - XBOX, 3 - Nintendo "))

playstation = 0
xbox = 0
nintendo = 0

if voto1 == 1:
    playstation = playstation + 1
elif voto1 == 2:
    xbox = xbox + 1
elif voto1 == 3:
    nintendo = nintendo + 1

if voto2 == 1:
    playstation = playstation + 1
elif voto2 == 2:
    xbox = xbox + 1
elif voto2 == 3:
    nintendo = nintendo + 1

if voto3 == 1:
    playstation = playstation + 1
elif voto3 == 2:
    xbox = xbox + 1
elif voto3 == 3:
    nintendo = nintendo + 1

if voto4 == 1:
    playstation = playstation + 1
elif voto4 == 2:
    xbox = xbox + 1
elif voto4 == 3:
    nintendo = nintendo + 1

if voto5 == 1:
    playstation = playstation + 1
elif voto5 == 2:
    xbox = xbox + 1
elif voto5 == 3:
    nintendo = nintendo + 1

if playstation > xbox and playstation > nintendo:
    print("O escolhido foi o Playstation com {} votos" .format(playstation))
elif xbox > nintendo and xbox > playstation:
    print("O escolhido foi o Xbox com {} votos".format(xbox))
elif nintendo > playstation and nintendo > xbox:
    print("O escolhido foi o Nintendo com {} votos".format(nintendo))

else:
    print("Não houve vencedor.")

