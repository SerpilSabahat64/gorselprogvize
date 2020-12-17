# Soru 3.
metin = "Bugün günlerden Perşembe"
aranan = "nle"
bulunan = metin.find(aranan)
if (bulunan > 0):
	pre = metin[bulunan - 1]
	post = metin[bulunan + len(aranan)]
	print(pre + aranan + post)
else:
	print("Aranan değer bulunamadı!")