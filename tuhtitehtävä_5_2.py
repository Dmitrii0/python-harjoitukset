#print("Minulla on tällaisia oireita:")
pääkipu= None
tulehdus= None
väsymys= None
print("TERVETULOA TERVEYSASEMALLE! 🏥")
while input("Mikä oire on sinulla? ") != "en tiedä":
    break
    if input("Onko sinulla vielä oireita? (kyllä/ei)") == "kyllä":
        pääkipu = input("Onko sinulla päänsärkyä? (kyllä/ei)")
        tulehdus = input("Onko sinulla tulehdusta? (kyllä/ei)")
        väsymys = input("Onko sinulla väsymystä? (kyllä/ei)")
    if pääkipu == "ei" and tulehdus == "ei" and väsymys == "ei":
        print("Sinulla ei ole oireita. Kiitos tiedoista. Sitten verinäytteet ja tutkimukset.")
    elif pääkipu == "kyllä" and tulehdus == "kyllä" and väsymys == "kyllä":
        print("Sinulla on oireita. Kiitos tiedoista. Sitten verinäytteet ja tutkimukset.")
print("Kiitos tiedoista. Sitten verinäytteet ja tutkimukset.")

#nimi = input("Anna nimi: ")
#diagnoosi = input("Anna diagnoosi: ")