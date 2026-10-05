import json

class Pelaaja:          #yläluokka
    def __init__(self, nimi):
        self.nimi = nimi
class Potilas(Pelaaja):  #aliluokka ja periytyminen
    def __init__(self, nimi, ikä, pituus, paino):
        super().__init__(nimi)
        self.ikä = ikä
        self.pituus = pituus
        self.paino = paino

class Lääkäri(Pelaaja):
    def __init__(self, nimi):
        super().__init__(nimi)

class Vastaanotto:
    def __init__(self, potilas, lääkäri):
        self.potilas = potilas
        self.lääkäri = lääkäri
    def näytä_tiedot(self):
        print("Potilaan tiedot: ")
        print("Nimi: " + self.potilas.nimi)
        print("Ikä: " + str(self.potilas.ikä))
        print("Pituus: " + str(self.potilas.pituus) + " cm")
        print("Paino: " + str(self.potilas.paino) + " kg")
        print("Lääkäri:" + self.lääkäri.nimi)

    def näytä_oma_tiedot(self):
        print("Nimi: " + self.potilas.nimi)
        print("Ikä: " + str(self.potilas.ikä))
        print("Pituus: " + str(self.potilas.pituus) + " cm")
        print("Paino: " + str(self.potilas.paino) + " kg")

def näytä_tutkimukset():
    print("Tehdyt tutkimukset: ")
    for tutkimus in tutkimukset:
        print("- " + tutkimus)



def mittaa_verenkokeeseen():
    verensokeri = float(input("Anna verensokeriarvosi: "))
    tutkimukset.append("Verenkokeen tulos: " + str(verensokeri))
    if verensokeri < 4.0:
        print("Verensokerisi on liian alhainen. ")
        diagnosoinnit.append("Verenkokeen tulos:   " + str(verensokeri)+ "(liian alhainen)")
    elif verensokeri <= 6.0:
        print("Verensokerisi on normaali.")
        diagnosoinnit.append("Verenkokeen tulos:   " + str(verensokeri)+ "(normaali)") 
    else:
        print("Verensokerisi on liian korkea.")  
        diagnosoinnit.append("Verenkokeen tulos:  " + str(verensokeri)+ "(liian korkea)")    

def mittaa_verenpaine():
    yläpaine = int(input("Anna yläpaineesi: "))
    alapaine = int(input("Anna alapaineesi: "))
    print("Yläpaine: " + str(yläpaine) + ", Alapaine: " + str(alapaine))
    tutkimukset.append("Verenpaine: " + str(yläpaine) + "/" + str(alapaine))
    if yläpaine > 140 or alapaine > 90:
        print("Verenpaineesi on korkea.")
        diagnosoinnit.append("Verenpaine: " + str(yläpaine) + "/" + str(alapaine) + " (korkea)")
    elif yläpaine < 90 or alapaine < 60:
        print("Verenpaineesi on matala.")
        diagnosoinnit.append("Verenpaine: " + str(yläpaine) + "/" + str(alapaine) + " (matala)")
    else:
        print("Verenpaineesi on normaali.")
        diagnosoinnit.append("Verenpaine: " + str(yläpaine) + "/" + str(alapaine) + " (normaali)")

def mene_vastaanotolle():
    print("Olet menossa vastaanotolle. Odota hetki...")
    print("Lääkäri " + lääkäri.nimi + " on valmis ottamaan sinut vastaan.")
    vastaanotto.näytä_tiedot()
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

def näytä_diagnosointi():
    print("Lääkärin diagnosointi: ")
    if len(diagnosoinnit) == 0:
        print("Ei diagnosointia saatavilla.")
    else:
        for diagnosointi in diagnosoinnit:
            print(" - " + diagnosointi)

def lääkärin_lopputarkastus():
    print("Lääkäri " + lääkäri.nimi + " on tarkastanut potilaan tiedot.")
    print("Potilaan tiedot: ")
    print(" - Nimi: " + potilas.nimi)
    print(" - Ikä: " + str(potilas.ikä))
    print(" - Pituus: " + str(potilas.pituus) + " cm")
    print(" - Paino: " + str(potilas.paino) + " kg")
    print("Tehdyt tutkimukset: ")
    if len(tutkimukset) == 0:
        print("Ei tutkimuksia saatavilla.")
    else:
        for tutkimus in tutkimukset:
            print(" - " + tutkimus)
    if len(diagnosoinnit) == 0:
        print("Ei diagnosointia saatavilla.")
    else:
        for diagnosointi in diagnosoinnit:
            print(" - " + diagnosointi)

def tallennus():
    print("Tallennetaan potilaan tiedot tiedostoon")
    tallennettavat_tiedot ={
        "nimi": potilas.nimi,
        "ikä": potilas.ikä,
        "pituus": potilas.pituus,
        "paino": potilas.paino,
        "tutkimukset": tutkimukset,
        "suositukset": suositukset,
        "diagnosoinnit": diagnosoinnit
    }
    with open("potilaan_tiedot.json", "w") as tiedosto:
        json.dump(tallennettavat_tiedot, tiedosto)

def lataa_tiedot():
    try:
        with open("potilaan_tiedot.json", "r") as tiedosto:
            tallennetut_tiedot = json.load(tiedosto)
        return tallennetut_tiedot
    except FileNotFoundError:
        return "Potilaan tiedosto ei löytynyt."

with open("intro.txt", "r") as tiedosto:
    intro = tiedosto.read()
    print(intro)

with open("ohjeet.txt", "r") as tiedosto:
    ohjeet = tiedosto.read()
    print(ohjeet)
    
jatka = input("Halutaanko jatkaa edellisestä tallennuksesta? (kyllä/ei): ")


if jatka == "kyllä":
    tiedot = lataa_tiedot()
    if isinstance(tiedot, dict):
        nimi = tiedot["nimi"]
        ikä = tiedot["ikä"]
        pituus = tiedot["pituus"]
        paino = tiedot["paino"]
        tutkimukset = tiedot["tutkimukset"]
        suositukset = tiedot["suositukset"]
        diagnosoinnit = tiedot["diagnosoinnit"]
    else:
        print(tiedot)
        exit()
else:
    nimi = str(input("Anna nimesi: "))
    ikä = int(input("Anna ikasi: "))
    pituus = float(input("Anna pituutesi (cm): "))
    paino = float(input("Anna painosi (kg): "))
    tutkimukset = []
    suositukset = []
    diagnosoinnit = []


potilas = Potilas(nimi, ikä, pituus, paino)
lääkäri = Lääkäri("Jussi")
vastaanotto = Vastaanotto(potilas, lääkäri)

if ikä < 12:
    print("Olet liian nuori pelaamaan tätä peliä")
    exit()
else:
    print("Tervetuloa pelaamaan peliä")


komento = ""

while komento != "lopeta":

    print("SAIRAALAPELI")
    print("1. Mene vastaanotolle")
    print("2. Mittaa verenpaineesi")
    print("3. Menee verenkokeeseen")
    print("4. Näytä oma tiedot")
    print("5. Näytä tehdyt tutkimukset")
    print("6. Näytä lääkärin suositukset")
    print("7. Näytä diagnosointi")
    print("8. Lääkärin loppitarkastus")
    print("9. Poista sairalasta")


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
        print("Näytä oma tiedot")
        vastaanotto.näytä_oma_tiedot()

    if komento == "5":
        print("Näytä tehdyt tutkimukset")
        näytä_tutkimukset()

    if komento == "6":
        print("Näytä lääkärin suositukset")
        näytä_suositukset()

    if komento == "7":
        print("Näytä diagnosointi")
        näytä_diagnosointi()

    if komento == "8":
        print("Lääkärin loppitarkastus")
        lääkärin_lopputarkastus()
        
    if komento == "9":
        tallennus()
        print("Poista sairalasta")
        poista_sairaalasta()
        break