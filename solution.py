import requests as Nug
from bs4 import BeautifulSoup
import re
from random import choice

resp = Nug.get("https://books.toscrape.com/")
soup = BeautifulSoup(resp.content, features="lxml")

book_tags = soup.find_all("article", attrs={"class": "product_pod"})

def clean_price(price):
    return float(re.sub("[^0-9.]", "", price))

def convert_rating(rating):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    return rating_map[rating]

def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][-1]

    return {
        "title": title,
        "price": clean_price(price),
        "rating": convert_rating(rating)
    }

randomdata = extract_book_data(choice(book_tags))

print(randomdata)