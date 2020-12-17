# Soru 4.
numara3digit = 123
occurCheck = ""
for i in str(numara3digit):
	occurCount = str(numara3digit).count(i)
	if (occurCount > 1):
		occurCheck += i
		if (occurCheck.count(i) == 1):
			print(i + " sayısı " + str(occurCount) + " defa kullanılmıştır")
if (len(occurCheck) == 0):
	print("Tekrarlayan sayı yok")