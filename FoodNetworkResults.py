from  bs4 import BeautifulSoup
import requests

def list_valid_Fn_Recipes(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="mod-site-search-results-1")

    print(soup)