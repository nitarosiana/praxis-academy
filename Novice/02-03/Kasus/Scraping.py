import requests

from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
bl = "https://www.tokopedia.com/discovery/flash-sale"
res = requests.get(bl, headers=header)
html = BeautifulSoup(res.content, "html.parser")
rows = html.find("div", class_ = "_1E0nAqju")
divs = rows.findAll("div", { "class" :"I8luE9wS"})
data = []
for div in divs:
	title = div.find("div", class_ = "_2A1s174V").text
	harga = div.find("div", class_ = "_2B_PeQak").text
	link = div.a.get("href")
	obj = {
		"nama" : title,
		"harga" : harga,
		"link" : link
	}
	data.append(obj)
print(data)