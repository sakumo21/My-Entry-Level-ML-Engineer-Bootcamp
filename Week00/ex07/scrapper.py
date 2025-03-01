import requests
from bs4 import BeautifulSoup

URL = "https://data.1337ai.org"
r = requests.get(URL)
print(type(r.content))
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.find_all('th'))
# print(soup.body.tr.children)
