from urllib import response
from bs4 import BeautifulSoup
import requests
import json 

url="http://books.toscrape.com"

response = requests.get(url)
htmlcontent=response.content

soup = BeautifulSoup(htmlcontent,'html.parser')

names=[]
prices=[]
availabilities=[]
photos=[]


for d in soup.find_all('li',attrs={'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'}):
    name=d.find('article',attrs={'class':'product_pod'})
    

    price=d.find('div',attrs={'class':'product_price'})
   
 
    availability=d.find('div',attrs={'class':'product_price'}).find('p',attrs={'class':'instock availability'})
    
    photo=d.find('article',attrs={'class':'product_pod'}).find('div',attrs={'class':'image_container'})
    print(photo)

    names.append(name.h3.a.get('title'))
    prices.append(price.p.string)
    availabilities.append(availability.text.strip())
    photos.append(photo.a.img.get('src'))

filename = 'result.json'                                          
with open(filename, 'w+') as file_object:                         
    json.dump(names + prices +availabilities +photos, file_object)
    
print(names)
print(prices)
print(availabilities)
print(photos)