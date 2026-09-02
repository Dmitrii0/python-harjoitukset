nimi = str(input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))

#print("Tervetuloa,", nimi, "!")


if ikä < 12:
    print("Olet liian nuori pelaamaan tätä peliä")
    exit()
else:
    print("Tervetuloa pelaamaan peliä")

komento = ""

while komento != "lopeta":

    #komento = input("Anna komento: ")

    #print("Tervetuloa,", nimi, "!")
    print("PÄÄVALIKKO")
    print("1. Aloita peli")
    print("2. Tutki sairalaa")
    print("3. Verenpaineen mittaus")
    print("4. Lopeta peli")

    komento = input("Anna komento: ")

    if komento == "1":
        print("Peli alkaa")

    if komento == "2":
        print("Tutki sairalaa")

    if komento == "3":
        print("Verenpaineen mittaus")

    if komento == "4":
        print("4. Lopeta peli")

    komento = input("Anna komento: ")
        