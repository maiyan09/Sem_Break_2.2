from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://books.toscrape.com/"

d = requests.get(url)

soup = BeautifulSoup(d.text, "html.parser")
# print(soup.prettify())
# with open("books.html", "w", encoding="utf-8") as f:
#     f.write(d.text)

books = soup.find_all('article', class_="product_pod") #article tag -> class =  product_pod
df = {
    "title": [],
    "price": [],
    "link": []
    }

for i in books:
    link = "https://books.toscrape.com/" + i.h3.a["href"]
    title = i.h3.a["title"]
    price = i.find("p", class_="price_color").text[1:]

    df["title"].append(title)
    df["price"].append(price)
    df["link"].append(link)
    
df = pd.DataFrame(df)
df.to_csv("Books.csv", index=False)