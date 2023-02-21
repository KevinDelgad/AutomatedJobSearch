from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests

def list_valid_fn_recipes(url):
    opts = ChromeOptions()
    opts.add_argument("--headless")
    browser = Chrome(options=opts)
    browser.get(url)
    results = browser.find_elements(By.CLASS_NAME,"o-RecipeResult")

    for recipe in results:
        link_url = recipe.find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(recipe.text)
        print(link_url)

def list_fn_recipe(url):
    opts = ChromeOptions()
    opts.add_argument("--headless")
    browser = Chrome(options=opts)
    browser.get(url)
    ingredients = browser.find_elements(By.CLASS_NAME, "o-Ingredients__a-Ingredient")
    for ingredient in ingredients:
        if(ingredient.text != "Deselect All"):
            print(ingredient.text)