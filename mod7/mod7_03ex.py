def bensiin_määrä():
    yksi_gallon = 3.785
    litrat = float(input("Anna bensiinimäärä litraina: "))
    gallonat = litrat / yksi_gallon
    print(f"Bensiinimäärä on {gallonat:.2f} gallonaa.")
    return gallonat