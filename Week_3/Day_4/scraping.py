from bs4 import BeautifulSoup
import requests
import json

url = "https://smsgadget.com/category/unofficial-phone"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

phones = []

for product in soup.select("div.p-item"):
    phone = {
        "name": product.select_one("h4.p-item-name a").get_text(strip=True),
        "price": product.select_one("span.price-new").get_text(strip=True),
        "url": product.select_one("h4.p-item-name a")["href"]
    }

    phones.append(phone)

with open("phones.json", "w", encoding="utf-8") as f:
    json.dump(phones, f, indent=4, ensure_ascii=False)