import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA"
yelp_r = requests.get(url)

print(yelp_r.status_code)

yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")
#print(yelp_soup.prettify())
#print(yelp_soup.findAll('a')) # Once HTML is parsed by BeatifulSoup, find all <a> tags.

for link in yelp_soup.findAll('a'):
    print(link)
