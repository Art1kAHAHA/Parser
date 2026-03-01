import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")  # lxml меняем на html.parser

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for i in range(len(quotes)):
    print(f"{quotes[i].text} — {authors[i].text}")
    print("-" * 50)


with open("цитаты.txt", "w", encoding="utf-8") as f:
    for i in range(len(quotes)):
        f.write(f"{quotes[i].text} - {authors[i].text}\n")
        f.write("-" * 50 + "\n")
print("Сохранено в файл цитаты.txt")