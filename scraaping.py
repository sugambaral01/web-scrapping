import requests
from bs4 import BeautifulSoup
link=requests.get("https://merojob.com/")
print(link) # this will print the that we can get the requests or not
#response 200 we can get it easily
soup=BeautifulSoup(link.text,'html.parser')
#print(soup.prettify())# this will print in good and clean format
box=soup.find_all('div',class_="col-md-4 border-right border-bottom job-card")
for div in box:
     classs=div.find('a',itemprop='title').text
     print(classs)













