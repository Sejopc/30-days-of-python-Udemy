import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import shutil
import time

driver = webdriver.Firefox()
driver.get("https://www.chrisburkard.com/Shop/Best-Sellers/")
html = driver.execute_script("return document.documentElement.outerHTML")
#print(html)
sel_soup = BeautifulSoup(html, 'html.parser')
print(len(sel_soup.findAll("img"))) # Now, it DOES grab ALL the images on the web page.

images = []
for i in sel_soup.findAll("img"):
    #print(i)
    src = i["src"]
    images.append(src)
    #print("++++++++++++++++++")
    #print(dir(i)) # All methods available for variable 'i'

print("---------------------")
print(images)

current_path = os.getcwd()

for img in images:
    try:
        file_name = os.path.basename(img)
        img_r = requests.get(img, stream=True) # stream=True is the key to download the images (the raw bytes)
        new_path = os.path.join(current_path, "images", file_name)
        with open(new_path, "wb") as output_file:
            shutil.copyfileobj(img_r.raw, output_file)
        del img_r
    except:
        pass
