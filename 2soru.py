# Soru 2.
# string func. kullanilmayacagi icin regular expression kullanildi.
import re

ornek = '^(http[s]?:\/\/)?([w]{3}\.)?[a-z0-9\._-]+[.]\w{2,3}([.]\w{2})?$'
def validateURL(adres):
    if (re.search(ornek, adres)):
    	print("---URL adresi doğrulandı---")
    else: 
    	print("---URL hatalı---!")

validateURL("www.google.com")