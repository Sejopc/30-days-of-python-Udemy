import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
loc = "San+Francisco,+CA"
page = 10
url = base_url + loc + "&start=" + str(page)

yelp_r = requests.get(url)

#print(yelp_r.status_code)

yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")

#print(yelp_soup.findAll('li', {'class': 'regular-search-result'}))
#print(yelp_soup.findAll('a', {'class': 'lemon--a__373c0__IEZFH'}))

#for name in yelp_soup.findAll('a', {'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}):
#    print(name.text)

#title = biz.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'})
#print(title.text)

file_path = 'yelp-{loc}.txt'.format(loc=loc)
with open(file_path,'a') as textfile:
    business = yelp_soup.findAll('div', {'class': 'lemon--div__373c0__1mboc scrollablePhotos__373c0__1LEvd arrange__373c0__2C9bH border-color--default__373c0__3-ifU'})
    for biz in business:
        #title_span  = biz.findAll('span', {'class':'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p'})
        title_a     = biz.findAll('a', {'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'})[0].text
        address     = biz.findAll('p', {'class':'lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO'})
        phone       = biz.findAll('p', {'class':'lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO'})[0].text
        if address == []:
            continue
        #print(address2)
        page_line = "{title_a}\n{address}\n{phone}\n-----------------\n".format(title_a=title_a, address=address[1].text + ", " +address[2].text, phone=phone)
        textfile.write(page_line)
