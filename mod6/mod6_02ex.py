luku = []
numero = input("Anna luku: ")
while numero != "":
    luku.append(int(numero))
    numero = input("Anna luku: ")
luku.sort(reverse=True)

for i in range(5):
    print(luku[i])