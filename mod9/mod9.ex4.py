import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus):
        self.tämänhetkinen_nopeus += nopeus
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * aika


class Kilpailu:
    def __init__(self,nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15)) 
            auto.kulje(1)
            auto.kiihdytä(muutos)




auto = Auto("ABC-123", 142)

print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.tämänhetkinen_nopeus)
print(auto.kuljettu_matka)

auto.kiihdytä(30)
print(auto.tämänhetkinen_nopeus)

auto.kiihdytä(70)
print(auto.tämänhetkinen_nopeus)

auto.kiihdytä(50)
print(auto.tämänhetkinen_nopeus)

auto.kiihdytä(-200)
print(auto.tämänhetkinen_nopeus)
