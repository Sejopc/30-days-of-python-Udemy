#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import requests
from bs4 import BeautifulSoup

url = "https://unsplash.com/s/photos/photography"

web_request = requests.get(url)
#print(web_request.text)
web_soup = BeautifulSoup(web_request.text, 'html.parser')
#print(len(web_soup.findAll("img")))


#### Above will NOT grab all the images because that's not what Requests library is meant for.
#### For a real web browser using terminal, we will need to use Selenium web driver, which will grab
#### Everything on the page for us.

#### Selenium is gonna open through Firefox.
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.chrisburkard.com/Shop/Best-Sellers/")
html = driver.execute_script("return document.documentElement.outerHTML")
#print(html)
sel_soup = BeautifulSoup(html, 'html.parser')
print(len(sel_soup.findAll("img"))) # Now, it DOES grab ALL the images on the web page.

images = []
for i in sel_soup.findAll("img"):
    print(i)
    src = i["src"]
    images.append(src)

print("---------------------")
print(images)
