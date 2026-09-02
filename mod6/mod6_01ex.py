import random
määrä= int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0
for i in range(määrä):
    arpo = random.randint(1, 6)
    summa += arpo
print("Arpakuutioiden summa on: ", summa)
    

