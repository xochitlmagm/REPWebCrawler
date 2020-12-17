"""
Web Scraper to gather Trulia real estate data with User Agent
Mustafa
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import os


state = input("State 2 letter abbrv: ")
town = input("City: ")
town = town.replace(" ", "_")

l = []
base_url = "https://www.trulia.com/" + state + "/" + town + "/"
for page in range(0, 3):

    c = urlopen(Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})).read()
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", attrs={"data-testid": "home-card-sale"})

    for item in all:
        d = {}
        try:
            d["Address"] = (item.find("div", attrs={"data-testid": "property-street"}).text)
            d["Town, State"] = (item.find("div", attrs={"data-testid": "property-region"}).text)
            d["Price"] = (item.find("div", attrs={"data-testid": "property-price"}).text.replace("+", ""))
            print(d["Price"])
            d["Beds"] = (item.find("div", attrs={"data-testid": "property-beds"}).text.replace('bd', ""))
            d["Sqft"] = (item.find("div", attrs={"data-testid": "property-floorSpace"}).text.replace(' sqft', ""))
            d["Baths"] = (item.find("div", attrs={"data-testid": "property-baths"}).text.replace('ba', ""))
        except:
            pass
        l.append(d)
    new_url = base_url + "/" + str(page) + "_p/"
    print(new_url)

# Used to convert data into a csv file


df = pd.DataFrame(l)
convert = "trulia_" + town + "_" + state + ".csv"
df.to_csv(convert)
print("Saved to " + os.getcwd() + " as " + convert)
