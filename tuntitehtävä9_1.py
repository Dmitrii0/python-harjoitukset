import random

inventaario = []

class Inventaario:
    def __init__(self):
        self.loitsut = []
        self.reppu = {}
        
    def lisätä(self, tavara):
        for tavara in self.reppu:
            print(f"Repun sisältö: {tavara}")
        self.reppu[tavara] = "hyvä"

    def laatu(self, tavara):
        if tavara in self.reppu:
            print(f"{tavara} on hyvässä kunnossa.")
        elif tavara in self.reppu:
            print(f"{tavara} on keskikertoisessa kunnossa.")
        else:
            print(f"{tavara} on huonossa kunnossa.")   

peli = Inventaario()
    
print("Lisää tavara reppuun: ")
tavara = input()
peli.lisätä(tavara)
        


