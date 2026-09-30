class Sairaus:
    def __init__(self,nimi, oireet):
        self.nimi = nimi
        self.oireet = oireet
        

class Potilas:
    def __init__(self, nimi, ikä, pituus, paino):
        self.nimi = nimi
        self.ikä = ikä
        self.pituus = pituus
        self.paino = paino

    

class Lääkäri:
    def __init__(self, nimi):
        self.nimi = nimi



def näytä_oma_tiedot():
    print("Nimi: " + potilas.nimi)
    print("Ikä: " + str(potilas.ikä))
    print("Pituus: " + str(potilas.pituus) + " cm")
    print("Paino: " + str(potilas.paino) + " kg")

def näytä_tutkimukset():
    print("Tehdyt tutkimukset: ")
    for tutkimus in tutkimukset:
        print("- " + tutkimus)

def tutki_sairaalaa():
    print("Olet sairalan tutkimassa.")


def mittaa_verenkokeeseen():
    verensokeri = float(input("Anna verensokeriarvosi: "))
    tutkimukset.append("Verenkokeen tulos: " + str(verensokeri))
    if verensokeri < 4.0:
        print("Verensokerisi on liian alhainen. ")
    elif verensokeri <= 6.0:
        print("Verensokerisi on normaali.")  
    else:
        print("Verensokerisi on liian korkea.")  

def mittaa_verenpaine():
    yläpaine = input("Anna yläpaineesi: ")
    alapaine = input("Anna alapaineesi: ")
    print("Yläpaine: " + yläpaine + ", Alapaine: " + alapaine)
    tutkimukset.append("Verenpaine: " + yläpaine + "/" + alapaine)

def mene_vastaanotolle():
    print("Olet menossa vastaanotolle. Odota hetki...")
    print("Lääkäri" + lääkäri.nimi + " on valmis ottamaan sinut vastaan.")
    print("1. Minulla on päänsärky")
    print("2. Minulla on väsyttävä olo")
    print("3. Haluan tarkistuttaa terveydentilani")

    valinta = input("Valitse oireesi (1-3): ")
    if valinta == "1":
        print("Lääkäri suosittelee sinulle verenpaineen mittamista ja lepoa.")
        suositukset.append("Verenpaineen mittaus")
        
    elif valinta == "2":
        print("Lääkäri suosittelee sinulle verenkokeen tekemistä.")
        suositukset.append("Verenkokeen tekeminen")
    elif valinta == "3":
        print("Lääkäri suosittelee sinulle terveydentarkastusta.")
        suositukset.append("Terveydentarkastus")

def poista_sairaalasta():
    print("Peli lopetetaan.")

def näytä_suositukset():
    print("Lääkärin suositukset: ")
    for suositus in suositukset:
        print(" - " + suositus)    
 
nimi = str(input("Anna nimesi: "))
ikä = int(input("Anna ikäsi: "))
pituus = float(input("Anna pituutesi (cm): "))
paino = float(input("Anna painosi (kg): "))

potilas = Potilas(nimi, ikä, pituus, paino)
lääkäri = Lääkäri("Jussi")

if ikä < 12:
    print("Olet liian nuori pelaamaan tätä peliä")
    exit()
else:
    print("Tervetuloa pelaamaan peliä")

tutkimukset = []    
suositukset = []

komento = ""

while komento != "lopeta":

    print("SAIRAALAPELI")
    print("1. Mene vastaanotolle")
    print("2. Mittaa verenpaineesi")
    print("3. Menee verenkokeeseen")
    print("4. Tutki sairaalaa")
    print("5. Näytä oma tiedot")
    print("6. Näytä tehdyt tutkimukset")
    print("7. Näytä lääkärin suositukset")
    print("8. Poista sairalasta")


    komento = input("Anna komento: ")

    if komento == "1":
        mene_vastaanotolle()

    if komento == "2":
        print("Mittaa verenpaineesi")
        mittaa_verenpaine()

    if komento == "3":
        print("Menee verenkokeeseen")
        mittaa_verenkokeeseen()

    if komento == "4":
        print("Tutki sairaalaa")
        tutki_sairaalaa()

    if komento == "5":
        print("Näytä oma tiedot")
        näytä_oma_tiedot()

    if komento == "6":
        print("Näytä tehdyt tutkimukset")
        näytä_tutkimukset()

    if komento == "7":
        print("Näytä lääkärin suositukset")
        näytä_suositukset()

    if komento == "8":
        print("Poista sairalasta")
        poista_sairaalasta()
        break