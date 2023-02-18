import requests
from bs4 import BeautifulSoup   

url = "https://www.allrecipes.com/search?q=pancakes"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="card-list_1-0")

recipes = results.find_all("a", class_="comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")

for card in recipes:
    title_elem = card.find(class_="card__title-text")
    is_recipe = card.find(class_="comp card__save mntl-save mntl-block")
    link = card.get("href")

    if(is_recipe != None):
        print(title_elem.text.strip())
        print(link)