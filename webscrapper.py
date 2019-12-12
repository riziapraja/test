import requests
from bs4 import BeautifulSoup

urls = input("input url : ")
page = requests.get(urls)

soup = BeautifulSoup(page.content, 'html.parser')

item_title = soup.find("h3", class_="tit-prd")
item_price = soup.find("span", class_="sellPrice")
item_option = soup.find_all("option")
title=item_title.text
price=item_price.text.strip()
c=[]
for item_option in item_option[1:]:
  c.append(item_option.text)
option = ('\n'.join(map(str, c)))
print(title)
print(price)
print(option)
