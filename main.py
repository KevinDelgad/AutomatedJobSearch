from allRecipesResultPage import list_All_Recipe, list_Valid_All_Recipes
from FoodNetworkResults import list_valid_Fn_Recipes

if __name__ == "__main__":
    url = "https://www.foodnetwork.com/search/tacos-"
    list_valid_Fn_Recipes(url)