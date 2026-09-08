def bensiin_määrä(gallonat):
    yksi_gallon = 3.785
    litrat = gallonat * yksi_gallon
    print(f"Bensiinimäärä on {litrat:.2f} litraa.")
    return litrat
while True:
    gallonat = float(input("Anna bensiinimäärä gallonina: "))
    if gallonat < 0:
        break
    litrat = bensiin_määrä(gallonat)