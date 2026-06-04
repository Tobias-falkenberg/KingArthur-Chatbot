import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("h3 a")

print("Number of books found:", len(books))

print("\nFirst 5 books:\n")

for book in books[:5]:
    print(book["title"])