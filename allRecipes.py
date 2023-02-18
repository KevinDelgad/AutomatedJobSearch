import requests
from bs4 import BeautifulSoup   

url = "https://www.allrecipes.com/recipe/6874/best-ever-muffins/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="jobsearch-ResultsList")

print(soup)