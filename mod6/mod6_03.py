luku = int(input("Anna kokonaisluku: "))


if luku == 1:
    print("Luku ei ole alkuluku")

else:
    for i in range(2, luku):
        if luku % i == 0:
            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")
    