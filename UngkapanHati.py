while True:
	aku = input("namaku : ")
	if aku == "":
		print("?")
	print("\nJadi " + ", Perasaan kamu ke dia gimana ?\n"
					  "1. cinta sama dia"
					  "2. sayang sama dia")
	pilihan = int(input("\nJawab: "))
	if pilihan == 1:
		print("\nDia: Kita temenan aja yah")
		continue
	elif pilihan == 2:
		print("\nDia : Maaf yah, aku udah punya pacar")
	else:
		print("hehe")