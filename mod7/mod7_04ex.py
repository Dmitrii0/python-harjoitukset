lista = [2, 4, 6, 7, 9]
    

def kokoluku(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

tulos = kokoluku(lista)
print(f"Alkuperäinen lista: {lista} . ")
print(f"Karsittu lista: {tulos} sisältää parilliset luvut. ")
