import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.90min.com/tr/posts/marca-ya-gore-2022-23-sezonunun-en-iyi-100-futbolcusu-01h4bdw7001h"

response = requests.get(url)

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

player_list= []

for i in soup.find_all("li",{"class":{"style_dswvvi"}}):
    player_list.append(i.text)
    print("Oyuncu Listesi",player_list)
    print("Oyuncu Sayısı",len(player_list))
    print("****************")