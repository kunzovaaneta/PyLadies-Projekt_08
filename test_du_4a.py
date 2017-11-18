from du_4a import stejna_zvirata()

seznam1=["kun", "ptak", "zirafa"]
seznam2=["kun", "zralok", "zirafa"]

seznam3=["kun", "zirafa"]

def test_stejna_zvirata():
	assert stejna_zvirata(seznam1, seznam2) == seznam3
