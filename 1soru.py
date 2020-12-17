# Soru 1.
# string func. kullanilmayacagi icin regular expression kullanildi.
import re

exp = '^[a-z0-9\._]+[@]\w+[.]\w{2,3}([.]\w{2})?$'
def validateEMail(dogrulama):
    if (re.search(exp, dogrulama)):
    	print("---E-Posta adresi doğru---")
    else: 
    	print("---E-Posta adresi yanlış!---")

validateEMail("serpilbasyigit.90@usak.edu.tr")