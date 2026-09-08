lentoasemat = {}
while True:
    valinta = input("1. Lisää lentoasema\n2. Hae lentoasema\n3. Lopeta\nValintasi: ")
    if valinta == "1":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi:")
        lentoasemat[koodi] = nimi
    elif valinta == "2":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        if koodi in lentoasemat:
            print(f"Lentoasema {koodi} on {lentoasemat[koodi]}.")
        else:
            print("Lentoasemaa ei löydy.")
    elif valinta == "3":
        break
    else:
        print("Virheellinen valinta.")
print("Lopetetaan.")
