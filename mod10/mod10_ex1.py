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
        if self.nykyinen < self.ylin_kerros:
            self.nykyinen += 1
        else:
            self.nykyinen += 1
        print(f"Nykyinen kerros: {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen - 1 >= self.alin_kerros:
            self.nykyinen -=1
        else:
            self.nykyinen -= 1
        print(f"Nykyinen kerros: {self.nykyinen}")

h = Hissi(1, 10) 
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)