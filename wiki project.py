import requests
import pprint
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/Main_Page'

page = requests.get(URL)

# pprint.pprint(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='mp-tfa')

# print(results.prettify())

linkinfo = results.find_all('a')

mainTitle = (linkinfo[1])

print(mainTitle.string)

for linkinfo in linkinfo:
    print(linkinfo.string)



# print(todaysArticle)