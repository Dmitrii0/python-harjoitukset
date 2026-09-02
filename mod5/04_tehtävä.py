from  random import randint, random

x = randint(1,10)
print(x)
user_input = 0
attempts = 0
while True:
    print("TERVETULOA ARVAUSPELIIN!")
    print("Arvaa luku väliltä 1-10: ")
    user_input = int(input("Sinun arvauksesi: "))
    attempts += 1
    if user_input < x:
        print("Liian suuri arvaus.")
    elif user_input > x:
        print("Liian pieni arvaus.")
    else:
        print(f"Oikein! Arvasit luvun {x} {attempts} yrityksessä.")
        break
