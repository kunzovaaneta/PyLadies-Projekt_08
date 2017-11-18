prvni_seznam_zvirat = ["pes", "kůň", "kočka", "papoušek"]
druhy_seznam_zvirat = ["pes", "kůň", "kočka", "papoušek"] 

def zvirata_pouze_v_prvnim_seznamu (prvni_seznam_zvirat, druhy_seznam_zvirat): 
	"""Zvířata, která jsou jen v prvním seznamu"""
	novy_seznam = prvni_seznam_zvirat	
	for prvni_zvirata in prvni_seznam_zvirat:
		for druha_zvirata in druhy_seznam_zvirat:
			if prvni_zvirata == druha_zvirata:# nevím proč podmínka funguje jen ob jednu položku v seznamu
				novy_seznam.remove(prvni_zvirata) # vyjmutím polozky ze seznamu se naruší poradí polozek, které procházejí podmínkou if 
			
	print(novy_seznam)

zvirata_pouze_v_prvnim_seznamu(prvni_seznam_zvirat, druhy_seznam_zvirat)