prvni_seznam_zvirat = ["pes", "kočka", "králík", "had"]
druhy_seznam_zvirat = ["papoušek", "myš", "prase", "had", "pes", "králík", "ježek"]

def stejna_zvirata(prvni_seznam_zvirat, druhy_seznam_zvirat):
	""" funkce, která vypíše zvířata, která jsou v obou seznamech"""
	seznam_spolecnych_zvirat= []
	for prvni_zvirata in prvni_seznam_zvirat:
		for druha_zvirata in druhy_seznam_zvirat:
			if prvni_zvirata == druha_zvirata:
				seznam_spolecnych_zvirat.append(prvni_zvirata)
	print (seznam_spolecnych_zvirat)


stejna_zvirata(prvni_seznam_zvirat,druhy_seznam_zvirat)




