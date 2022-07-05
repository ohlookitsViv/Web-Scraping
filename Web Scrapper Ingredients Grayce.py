import re
from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.delish.com/cooking/recipe-ideas/recipes/a51578/loaded-burrito-bowls-recipe/').text
soup = BeautifulSoup(source, 'lxml')

ingredient = soup.find("div", {"class": "ingredient-lists"})
ingredient2 = ingredient.find_all("div", {"class": "ingredient-item"})

 
ingredientlist = []

for ing in ingredient2:
    desc = ing.find("span", {"class": "ingredient-description"})
    ingredientlist.append(desc.text)


amountlist = []
length = len(ingredientlist)
y = 0
while length > y:
    for inger in ingredient2:
        if inger.find("span", {"class": "ingredient-amount"}):
            amount = inger.find("span", {"class": "ingredient-amount"})
            amountlist.append(amount.text)
            amountlist[y] = amountlist[y].replace("\t",'')
            amountlist[y] = amountlist[y].replace("\n",'')
            y = y+1
        else:
            amountlist.append(" ")
            y = y+1
            
print(amountlist)
print(ingredientlist)


