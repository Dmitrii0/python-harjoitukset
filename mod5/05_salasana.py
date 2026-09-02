yritykset = 0

while yritykset < 5:
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if käyttäjätunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    yritykset += 1
    if yritykset < 5:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

if yritykset == 5:
    print("Pääsy estetty: liian monta virheellistä yritystä.")
    