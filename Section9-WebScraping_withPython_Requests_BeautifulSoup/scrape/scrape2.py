import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?cflt=restaurants&find_loc="
loc = "San Francisco, CA"
page = 10
url = base_url + loc + "&start=" + str(page)

yelp_r = requests.get(url)

#print(yelp_r.status_code)

yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")

#print(yelp_soup.findAll('li', {'class': 'regular-search-result'}))
#print(yelp_soup.findAll('a', {'class': 'lemon--a__373c0__IEZFH'}))

for name in yelp_soup.findAll('a', {'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}):
    print(name.text)
