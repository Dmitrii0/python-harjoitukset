class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    

class Kirja(Julkaisu):

    def __init__(self, nimi,kirjottaja, sivumäärä):
        super().__init__(nimi)
        self.kirjottaja = kirjottaja
        self.sivumäärä = sivumäärä
    

    def tulosta_tiedot(self):
            print(f"Kirjottaja: {self.kirjottaja}, ja nimi: {self.nimi}, sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
    

    def tulosta_tiedot(self):
            print(f"Nimi: {self.nimi}, päätoimittaja:{self.päätoimittaja}")


lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti n:0 6", "Rosa Liksom", 200)

lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()