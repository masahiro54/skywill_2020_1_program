import requests
from bs4 import BeautifulSoup
import csv
import re

res = requests.get('https://tabelog.com/tokyo/A1329/A132901/13163640/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=5')
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
f = open('yururi_Review_5.csv', 'w',encoding="utf-8_sig")
for a in soup.find_all('a',class_="rvw-item__title-target"):
    url_Latter=a.get('href')
    url = 'https://tabelog.com' + url_Latter
    res_2 = requests.get(url)
    soup_2 = BeautifulSoup(res_2.text, 'html.parser')
    title = soup_2.find_all("div", class_="rvw-item__rvw-comment")
    csvlist = []
    for p in title:
      text_2 = p.text.replace(" ","")
      text_3 = text_2.replace("\n","")
      print(text_3+'\n')
      csvlist.append(text_3)

    writer = csv.writer(f,lineterminator='\n')
    writer.writerow(csvlist)

# ファイルクローズ
f.close()