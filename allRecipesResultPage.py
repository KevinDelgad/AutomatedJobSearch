import requests
from bs4 import BeautifulSoup   

# Grab all valid recipies from search pages
def list_valid_all_recipes(url):
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

#Grab amd Split Recipe into ingredients and instructions
def list_all_recipe(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    ingredients_list = soup.find(id="mntl-structured-ingredients_1-0")
    instructions = soup.find(id="recipe__steps_1-0")

    ingredients = ingredients_list.find_all("li", class_="mntl-structured-ingredients__list-item")
    for ingredient in ingredients:
        print(ingredient.text.strip())

    for step in instructions:
        print(step.text.strip())