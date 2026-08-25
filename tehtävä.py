ikä = int(input("Anna ikäsi: "))
laji = input("Anna lajisi i(ihminen)/t(tonttu)/r(robotti)")

print("Voit tilata:")
print("Sinä voit tilata kahvia")

if ikä >= 18 and laji == "i":
    print("Sinä voit tilata viiniä")
if ikä <= 100 and laji == "t" :
    print("Sinä voit tilata olutta")
if laji == "r":
    print("Sinä voit tilata öljä")       
  ##yhtä suuri kuin
  # >= suurempi tai yhtäsuuri kuin
  # <=  pienempi tai yhtäsuuri kuin