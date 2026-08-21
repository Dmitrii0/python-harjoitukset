leivisköinä = int(input("Anna leiviskät määrä:"))
nauloina = int(input("Anna naulat määrä: "))
luotia = float(input("Anna luodit määrä:"))
massa = leivisköinä * 20 + nauloina * 32 + luotia * 13.3

print("Leivisköitä: ", leivisköinä)
print("Nauloja: ", nauloina)
print("Luoteja: ", luotia)

kilot = int(massa // 1000)
grammat = massa % 1000

print("Massa yhteensä:", kilot, "kg ja", grammat, "g")