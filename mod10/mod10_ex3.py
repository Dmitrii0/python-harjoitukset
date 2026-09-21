class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen = alin_kerros



    def siirry_kerrokseen(self, kerros):
       while self.nykyinen != kerros:
        if self.nykyinen < kerros:
               self.kerros_ylös()
        else:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen  < self.ylin_kerros:
            self.nykyinen += 1
        print(f"Nykyinen kerros: {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen  > self.alin_kerros:
            self.nykyinen -= 1
        print(f"Nykyinen kerros: {self.nykyinen}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.ylös = ylin_kerros
        self.alas = alin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissi = []
        for i in range(hissien_määrä):
            self.hissi.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kerros):
        self.hissi[hissin_numero - 1].siirry_kerrokseen(kerros)

    def palohälytys(self):
        for hissi in self.hissi:
            hissi.siirry_kerrokseen(self.alas)

talo1 = Talo(1, 10, 3)
talo1.aja_hissia(2, 4)

talo1.palohälytys()