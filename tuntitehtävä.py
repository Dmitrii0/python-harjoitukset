#juoma_lista = 


ikä = int(input("Anna ikäsi: "))
laji = input("Anna lajisi i(ihminen)/t(tonttu)/r(robotti)")
print("Voit tilata kahvia")
if ikä >= 18 and laji == "i" and ikä == 18:
    print("Sinä voit tilata viiniä")
elif ikä <= 100 and laji == "t":
    print("Sinä voit tilata olutta")
elif laji == "r" and laji == "r":
    print("Sinä voit tilata öljä")
#else:
#    print("Sinä ei voi tilata ")