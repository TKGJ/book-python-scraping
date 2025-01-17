# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://api.aoikujira.com/zip/xml/1500042"

# urlopen()でデータを取得 --- (※1)
res = req.urlopen(url)

# BeautifulSoupで解析 --- (※2)
soup = BeautifulSoup(res, "html.parser")

# 任意のデータを抽出 --- (※3)
kenkana = soup.find("kenkana").string
ken = soup.find("ken").string
shi = soup.find("shi").string
cho = soup.find("cho").string
zip = soup.find("zip").string
print(kenkana,ken, shi, cho,zip)
