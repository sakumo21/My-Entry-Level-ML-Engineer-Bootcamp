import requests
from bs4 import BeautifulSoup
import csv

URL = "https://data.1337ai.org"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
with open("data.csv", "w") as file:
    for item in soup.find_all("tr"):
        file.write(",".join([x.text for x in item]) + '\n')

