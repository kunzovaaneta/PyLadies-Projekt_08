seznam_zvirat = ["pes", "kočka", "králík", "had"]

def kratka_jmena_zvirat(seznam):
	"""Funkce vypíše jména zvířat, která jsou kratší než 5 písmen"""
	for polozka in seznam:
		if len(polozka) < 5:
			print (polozka)

kratka_jmena_zvirat(seznam_zvirat)