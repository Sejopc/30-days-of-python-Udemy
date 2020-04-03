import requests
from bs4 import BeautifulSoup
import argparse
import urllib.parse

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
#loc = "San+Francisco,+CA"

parser = argparse.ArgumentParser(prog="scrape4.py")
parser.add_argument('-l', '--loc', type=str, required=True, help='Pass the location to look up for restaurants. The format is: city,state[,country name]. Eg:\n$python scrape4.py -l "San Francisco, CA"')
args = parser.parse_args()

def look_up_location(loc):
    current_page = 0
    while current_page < 201:
        url = base_url + loc + "&start=" + str(current_page)
        yelp_r = requests.get(url)
        yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")
        file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
        business = yelp_soup.findAll('div', {'class': 'lemon--div__373c0__1mboc scrollablePhotos__373c0__1LEvd arrange__373c0__2C9bH border-color--default__373c0__3-ifU'})
        try:
            with open(file_path,'a') as textfile:
                for biz in business:
                    title_a     = biz.findAll('a', {'class': 'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'})[0].text
                    address     = biz.findAll('p', {'class':'lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO'})
                    phone       = biz.findAll('p', {'class':'lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO'})[0].text
                    if address == [] or title_a == "" or phone == "":
                        continue
                    page_line = "{title_a}\n{address}\n{phone}\n-----------------\n".format(title_a=title_a, address=address[1].text + ", " +address[2].text, phone=phone)
                    textfile.write(page_line)
                #print("------>>>>>" + str(current_page) + "<<<<<-------")
                current_page+=10
        except(IndexError):
            current_page+=10
            pass

if args.loc:
    encoded_loc = urllib.parse.quote(args.loc)
    look_up_location(encoded_loc)

else:
    print("You are missing the LOCATION argument (--loc).")
