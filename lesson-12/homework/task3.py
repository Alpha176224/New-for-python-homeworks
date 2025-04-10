# Task 3: Scraping Demoblaze laptop data into JSON
import requests
from bs4 import BeautifulSoup
import json
from time import sleep

url = "https://www.demoblaze.com/index.html"
base = "https://www.demoblaze.com/"
session = requests.Session()
session.get(url)

def get_laptops(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    items = soup.find_all("div", class_="card h-100")
    laptops = []
    for item in items:
        name = item.find("a", class_="hrefch").text.strip()
        price = item.find("h5").text.strip()
        desc = item.find("p", class_="card-text").text.strip()
        laptops.append({
            "name": name,
            "price": price,
            "description": desc
        })
    return laptops

laptop_data = []
response = session.get("https://www.demoblaze.com/")
laptop_data.extend(get_laptops(response.text))

session.get("https://www.demoblaze.com/")
sleep(2)
session.post("https://www.demoblaze.com/bycat", json={"cat":"notebook"})
sleep(2)
session.get("https://www.demoblaze.com/")
next_page = session.get("https://www.demoblaze.com/")
laptop_data.extend(get_laptops(next_page.text))

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptop_data, f, indent=2, ensure_ascii=False)
