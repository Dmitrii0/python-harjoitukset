sukupuoli = input("Anna sukupuoli (m/n): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "m":
    if hemoglobiini < 134:
        print("Sinulla on alhainen hemoglobiiniarvo")
    elif hemoglobiini <= 195:
        print("Sinulla on normaali hemoglobiiniarvo")
    else:
        print("Sinulla on korkea hemoglobiiniarvo")

elif sukupuoli == "n":
    if hemoglobiini < 117:
        print("Sinulla on alhainen hemoglobiiniarvo")
    elif hemoglobiini <= 175:
        print("Sinulla on normaali hemoglobiiniarvo")
    else:
        print("Sinulla on korkea hemoglobiiniarvo")

else:
    print("Virheellinen sukupuoli")