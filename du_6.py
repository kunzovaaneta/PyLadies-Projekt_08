seznam_zvirat = ["pes", "kočka", "králík", "had", "andulka"] 

upraveny_seznam= []
for zvire in seznam_zvirat:
	upravene_zvire = zvire[1:]
	upraveny_seznam.append(upravene_zvire)

print (upraveny_seznam)
upraveny_seznam.sort()
print(upraveny_seznam)

seznam_zvirat_s_klicem=[]

for i, zvire_bez in enumerate(upraveny_seznam):#zasekla jsem se u vytvoření dvojic (klíč, hodnota)
	s = (i, zvire_bez)
	seznam_zvirat_s_klicem.append(s)
print (seznam_zvirat_s_klicem)
