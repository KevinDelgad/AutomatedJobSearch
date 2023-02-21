from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests

def list_valid_tasty_recipes(url):
    opts = ChromeOptions()
    opts.add_argument("--headless")
    browser = Chrome(options=opts)
    browser.get(url)
    recipes = browser.find_elements(By.CLASS_NAME, "feed-item__title ")
    for recipe in recipes:
        print(recipe.text)

def list_tasty_recipe(url):
    opts = ChromeOptions()
    opts.add_argument("--headless")
    browser = Chrome(options=opts)
    browser.get(url)
    yields = browser.find_element(By.CLASS_NAME, "servings-display")
    print(yields.text)
    ingredients_section = browser.find_element(By.CLASS_NAME, "ingredients__section")
    ingredients = ingredients_section.find_elements(By.CLASS_NAME, "ingredient")
    for ingredient in ingredients:
        print(ingredient.text)

    steps_section = browser.find_element(By.CLASS_NAME, "prep-steps")
    steps = steps_section.find_elements(By.CLASS_NAME, "xs-mb2")

    for step in steps:
        print(step.text)