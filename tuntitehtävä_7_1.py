def averages(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
        
    keskiarvo = summa / len(luvut)
    return keskiarvo

lista = [1, 2.3, 3.4, 56, 7.8, 9.0, 8, 10.12, 12]
tulos = averages(lista)
#print(f"Keskiarvo on: {tulos:.3f}")
print("Keskiarvo on: {f:.2f}".format(f=tulos))

#=yhtä kuin
# summa jaettuna listan puutuudella 
#{}aaltosulkeet