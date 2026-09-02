import random

piste = int(input("Kuinka monta pistettä haluat arpoa: "))
pisteet = 0
sisällä = 0
while pisteet < piste:
 x = random.uniform(-1, 1)
 y = random.uniform(-1, 1)
 pisteet +=1
 if x**2 + y**2 < 1:
   sisällä += 1

else:
    print("Piin likiarvo on: ", sisällä * 4 / piste)