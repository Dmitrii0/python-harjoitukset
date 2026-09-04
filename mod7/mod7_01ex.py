import random

def nopanheitto():
    heitto = random.randint(1, 6)
    return heitto

tulos = nopanheitto()
print(tulos)

while True:
    tulos = nopanheitto()
    print(tulos)
    if tulos == 6:
        break