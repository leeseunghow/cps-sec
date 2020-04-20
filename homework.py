import requests
from bs4 import BeautifulSoup
req = requests.get("https://search.shopping.naver.com/search/category.nhn?brand=240&spec=M10012483%7CM10574775%5EM10012483%7CM10197460%5EM10012483%7CM10574779%5EM10012483%7CM10614291%5EM10012483%7CM10614292%5EM10012483%7CM10030853&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=50000806&frm=NVSHATT")
if req.status_code != 200 :
    print("failed", req.status_code)

html = req.text
bs = BeautifulSoup(html, "html.parser")

box = bs.find_all("div", class_="info")

title = []
price = []
date = []

for b in box:
    title.append(b.find("div", class_="tit").find("a").text)
    price.append(b.find("span", class_="price").find("em").text)
    date.append(b.find("span", class_="etc").find("span",class_="date").text.split(" ")[1])


productinfo = []
for i in range(len(box)) : 
    product = []
    product.append(title[i])
    product.append(price[i])
    product.append(date[i])
    productinfo.append(product)
 #   productinfo.append([title[i], price[i], date[i]])

for i in productinfo :
    print(i)