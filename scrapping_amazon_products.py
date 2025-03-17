import requests
from bs4 import BeautifulSoup
link=requests.get("https://froxjob.com/explore-jobs")
print(link) # this will givw the request that we can scrap it or not
soup=BeautifulSoup(link.text,'html.parser')
#print(soup.prettify())
container=soup.find_all('div',class_='media-body')
for i in container:
    name=i.find('h6',class_='media-heading').text
    job_type=i.find('a',target='_blank').text
    linkss=container.ul.li.a['href']
    print(f'name of the job :{name} ') # this will print the name of the text
    print(f'job_type : {job_type}  ') # this will print the required job type that for the application 
    print(linkss)


    print('\n') # this will print in the new lines 




