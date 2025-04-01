import random

numero_secreto = random.randint(1, 100)

print("Tente adivinhar o número entre 1 e 100!")

while True:
    tentativa = int(input("Seu palpite: "))
    if tentativa < numero_secreto:
        print("Calmaaaa, esta muito baixo! ;(")
    elif tentativa > numero_secreto:
        print("jaja estamos nas nuvens em, Estamos Muito alto!")
    else:
        print("Parabéns, você esta igual o flamengo, campeao!")
        break
