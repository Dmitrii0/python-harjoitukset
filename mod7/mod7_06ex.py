import math


def pizza(halkaisija, hinta):
    halkaisija_m = halkaisija / 100
    pinta_ala = math.pi * (halkaisija_m / 2) ** 2
    hinta_per_m2 = hinta / pinta_ala
    return hinta_per_m2

halkaisija1 = float(input("Anna pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna pizzan hinta euroina: "))

halkaisija2 = float(input("Anna pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna pizzan hinta euroina: "))




hinta_per_m2_1 = pizza(halkaisija1, hinta1)
print(f"Pizzan hinta per neliömetri on {hinta_per_m2_1:.2f} euroa.")

hinta_per_m2_2 = pizza(halkaisija2, hinta2)
print(f"Pizzan hinta per neliömetri on {hinta_per_m2_2:.2f} euroa.")

if hinta_per_m2_1 < hinta_per_m2_2:
        print("Ensimmöinen pizza on edullisempi.")
elif hinta_per_m2_1 > hinta_per_m2_2:
    print("Toinen pizza on edullisempi.")
else:
     print("Molemmat pizzat ovat yhtä edullisia.")