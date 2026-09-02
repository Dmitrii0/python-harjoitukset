while True:
	tuumia = int(input("Anna tuumien määrä: "))

	if tuumia < 0:
		print("Ohjelma lopetetaan.")
		break

	sentimetri = tuumia * 2.54
	print("Tuumien määrä on", sentimetri, "cm")