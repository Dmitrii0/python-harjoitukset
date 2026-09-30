try:
    jakolasku1 = int(input("Kirjoita kaksi lukua: "))
    jakolasku2 = int(input("Kirjoita toinen luku: "))
    print("Lukujen summa on:  ", (jakolasku1 / jakolasku2))

except ValueError:
    print("Virhe: syötetty arvo ei ole kokonaisluku. Yritä uudestaan.")
    
except ZeroDivisionError:
        print("Virhe: jakaminen nollalla ei ole sallittua. Yritä uudestaan.")       