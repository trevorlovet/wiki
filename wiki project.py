import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Main_Page'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='mp-tfa')

#Getting All Links
link_info = results.find_all('a')

mainTitle = (link_info[1])

# To block out for unwanted words -- only works for the final two
do_not_print = ["None", "By email", "More featured articles", "Archive", "Full article..."]

print("Today's Wikipedia Article is about: " + mainTitle.string)

print("Other Topics include:   ")
for link_info in link_info:
    if link_info.string in do_not_print:
        continue
    else:
        print(link_info.string)
