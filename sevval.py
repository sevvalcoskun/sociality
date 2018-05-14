from urllib.request import urlopen
from bs4 import BeautifulSoup

wiki = "https://www.hepsiburada.com/asus-x542ur-gq030-intel-core-i7-7500u-8gb-1tb-gt930mx-freedos-15-6-tasinabilir-bilgisayar-p-HBV000008OBG5"

page = urlopen(wiki)
soup =  BeautifulSoup(page, "html.parser" )

valuesv = soup.find_all("del", attrs={'class': 'product-old-price price old'})[-1].getText()


print("Giriş değeri: " + wiki)
print("Sonuç: " + valuesv)

readln();

