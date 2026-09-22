class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

      


class Sähköauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
    

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus,huippunopeus, bensankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensankin_koko = bensankin_koko
   
sähköauto1 = Sähköauto("ABC-15", 180, 52.5)
bensaauto1 = Polttomoottoriauto("ACD-123", 165, 32.3)  

sähköauto1.kiihdytä(100)
bensaauto1.kiihdytä(80)

sähköauto1.kulje(3)
bensaauto1.kulje(3)

print(sähköauto1.kuljettu_matka)
print(bensaauto1.kuljettu_matka)