seznam_zvirat = ["pes", "kočka", "králík", "had"]

def kontrola_seznamu(seznam):
	"""Funkce zjistí, zda napsané slovo je či není v seznamu"""
	kontrolni_slovo = (input("Zadej zvíře, které chceš zkontrolovat, zda se nachází v seznamu: ")).lower()

	if kontrolni_slovo in seznam:
		print("Ano, slovo {} je v seznamu zvířat".format (kontrolni_slovo))
	else:
		print("Bohužel, toto zvíře není v seznamu")

kontrola_seznamu(seznam_zvirat)