import requests
import sys
url = "http://api.frankfurter.app/latest?from="

birinci_doviz = input("Birimic Döviz:")
ikinci_doviz = input("İkinci Döviz:")
miktar = float (input("Miktar:"))

response = requests.get(url + birinci_doviz)

json_verisi = response.json()

try:
        print(json_verisi["rates"][ikinci_doviz])
except KeyError:
    sys.stderr.write("Geçerli Bir Para Birimi Giriniz")
    sys.stderr.flush()