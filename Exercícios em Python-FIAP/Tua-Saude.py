idade = int(input("Informe a sua idade: "))
bpm = int(input("Informe o seu número de batimentos por minuto (BPM): "))

if idade <= 2 and 120 <= bpm <= 140:
    print("Seus batimentos cardiacos estão dentro da faixa adequada.")
elif idade <= 2 and bpm < 120:
    print("Seus batimentos cardiacos estão abaixo da faixa adequada.")
elif idade <= 2 and bpm > 140:
    print("Seus batimentos cardiacos estão acima da faixa adequada.")

if 8 <= idade <= 17 and 80 <= bpm <= 100:
    print("Seus batimentos cardiacos estão dentro da faixa adequada.")
elif 8 <= idade <= 17 and bpm < 80:
    print("Seus batimentos cardiacos estão abaixo da faixa adequada.")
elif 8 <= idade <= 17 and bpm > 100:
    print("Seus batimentos cardiacos estão acima da faixa adequada.")

if 18 <= idade <= 65 and 70 <= bpm <= 80:
    print("Seus batimentos cardiacos estão dentro da faixa adequada.")
elif 18 <= idade <= 65 and bpm < 70:
    print("Seus batimentos cardiacos estão abaixo da faixa adequada.")
elif 18 <= idade <= 65 and bpm > 80:
    print("Seus batimentos cardiacos estão acima da faixa adequada.")

if idade > 65 and 50 <= bpm <= 60:
    print("Seus batimentos cardiacos estão dentro da faixa adequada.")
elif idade > 65 and bpm < 50:
    print("Seus batimentos cardiacos estão abaixo da faixa adequada.")
elif idade > 65 and bpm > 60:
    print("Seus batimentos cardiacos estão acima da faixa adequada.")