import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Main_Page'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='mp-tfa')

linkinfo = results.find_all('a')

mainTitle = (linkinfo[1])

print("Todays Wikipedia Article is about: " + mainTitle.string)

print("Other Topics include:   ")
for linkinfo in linkinfo:
    print((linkinfo.string) )
