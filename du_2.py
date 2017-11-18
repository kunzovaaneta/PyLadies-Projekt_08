seznam_zvirat = ["pes", "kočka", "králík", "had"]

def zacatecni_pismeno_zvirete(seznam):
	"""Funkce vypíše jména domácích zvířat, které začínají na písmeno "k" """
	for polozka in seznam:
		if polozka[0] == "k":
			print (polozka)

zacatecni_pismeno_zvirete(seznam_zvirat)