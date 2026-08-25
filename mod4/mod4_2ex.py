hyttiluokka = input("Anna hyttiluokka (LUX, A, B, C): ")
if hyttiluokka == "LUX":
    print("Hyttiluokka on LUX, parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("Hyttiluokka on A, parvekkeellinen hytti autokannella.")
elif hyttiluokka == "B":
    print("Hyttiluokka on B, ikkunallinen hytti  yläpuolella..")
elif hyttiluokka == "C":
    print("Hyttiluokka on C, ikkunallinen hytti alapuolella.")
else:
    print("Virheellinen hyttiluokka.")