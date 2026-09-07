inventari = []

def näytä_inventari():
    print("Inventaarisi:")
    for item in inventari:
        print("- " + item)

    if not inventari:
        print("Inventaarisi on tyhjä.")

def lisää():
    item = input("Anna esineen nimi:")
    inventari.append(item)


def mittaa_verenpaine():
    yläpaine = input("Anna yläpaineesi: ")
    alapaine = input("Anna alapaineesi: ")
    print("Yläpaine: " + yläpaine + ", Alapaine: " + alapaine)

def aloita_peli():
    print("Peli alkaa!")

def lopeta_peli():
    print("Peli lopetetaan.")
 
nimi = str(input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))


if ikä < 12:
    print("Olet liian nuori pelaamaan tätä peliä")
    exit()
else:
    print("Tervetuloa pelaamaan peliä")

komento = ""

while komento != "lopeta":

    print("PÄÄVALIKKO")
    print("1. Aloita peli")
    print("2. Tutki sairaalaa")
    print("3. Verenpaineen mittaus")
    print("4. Lopeta peli")
    print("5. Näytä inventaario")

    komento = input("Anna komento: ")

    if komento == "1":
        aloita_peli()

    if komento == "2":
        print("Tutki sairaalaa")
        lisää()

    if komento == "3":
        print("Verenpaineen mittaus")
        mittaa_verenpaine()

    if komento == "4":
        lopeta_peli()
        exit()

    if komento == "5":
        näytä_inventari()
    