class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
         return(f"Julkaisun nimi: {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, nimi,kirjottaja, sivumäärä):
        super().__init__(nimi)
        self.kirjottaja = kirjottaja
        self.sivumäärä = sivumäärä
    

    def tulosta_tiedot(self):
            return(f"Kirjottaja: {self.kirjottaja}, ja nimi: {self.nimi}, sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
    

    def tulosta_tiedot(self):
            for Hylly in kirjasto:
                 print("On hyllyssä")
            else:
                 print("On lainassa")
kirjasto = []

try:
    with open("save.txt", "r") as tiedosto:
        data = tiedosto.read()
except FileNotFoundError:
    print("Tiedostoa ei löydy.")
          

  