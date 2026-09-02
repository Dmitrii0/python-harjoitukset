
vuosi = int(input("Anna vuosi: "))
while vuosi >= 1896:
    if vuosi % 4 == 0:
        print("Vuosi: " + str(vuosi) + " oli olympialaisvuosi.")
    else:
        print("Vuosi: " + str(vuosi) + " ei ollut olympialaisvuosi.")
    vuosi -= 1
print("Ohjelma ohi.")        

