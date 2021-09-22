import requests
from bs4 import BeautifulSoup
# Load the source code
r = requests.get("https://pythonizing.github.io/data/example.html",
                 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                                        'rv:61.0) Gecko/20100101Firefox/61.0'})

c = r.content

soup = BeautifulSoup(c,"html.parser")
# Indexing is supported
cities_only = []
all_cities = soup.find_all("div", {"class": "cities"})
for city in all_cities:
    cities_only.append(city.find("h2").text)

print(cities_only)

# print(soup.prettify())