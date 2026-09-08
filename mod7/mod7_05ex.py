lista = [2, 5, 7, 8, 12, 17, 18, 22, 34, 56, 45, 76, 69, 75, 84, 90, 102]

def kokoluku(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

tulos = kokoluku(lista) 
print(f"Alkuperäinen lista: {lista} . ")   
print(f"Karsittu lista: {tulos} sisältää parilliset luvut.")    