import random

def nopanheitto():
    heitto = random.randint(1, 6)
    return heitto

tulos = nopanheitto()
print(tulos)

maksimi = int(input("Anna maksimuluku: "))

while True:
    tulos = nopanheitto(maksimi)
    print(tulos)
    if tulos == maksimi:
        break