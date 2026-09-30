class Pelaaja:
    def __init__(self, nimi, taso, esineet):
        self.nimi = nimi
        self.taso = taso
        self.esineet = esineet

class Esine:
    def __init__(self, nimi, hinta):
        self.nimi = nimi
        self.hinta = hinta

esineet = [Esine("Miekka", 123), Esine("Kilpi", 100)]
pelaaja1 = Pelaaja("Arthur", 0, esineet)
print(pelaaja1.esineet)