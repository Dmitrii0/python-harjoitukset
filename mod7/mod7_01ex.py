import random


def nopanheitto(maksimi):
    heitto = random.randint(1, maksimi)
    return heitto
maksimi = int(input("Anna maksimuluku: "))

while True:
    tulos = nopanheitto(maksimi)
    print(tulos)
    if tulos == maksimi:
        break