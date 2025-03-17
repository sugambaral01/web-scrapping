import requests
from bs4 import BeautifulSoup
link=requests.get("https://www.jobsnepal.com/jobs")
print(link) # this will givw the request that we can scrap it or not
soup=BeautifulSoup(link.text,'html.parser')
#print(soup.prettify())
container=soup.find_all('div',class_='card-body')
for i in container:
    name=i.find('h2',class_='job-title').text
    About_jobs_type=i.find('div',class_='d-flex align-items-center pl-1 pr-1 py-1').text
    linkss=i.find('a')['href']
    if "Kathmandu" in About_jobs_type:
        print(f'name of the job :{name.strip()} ') # this will print the name of the text
        print(f'job_type : {About_jobs_type.strip()}  ') # this will print the required job type that for the application 
        print(f'Links:{linkss.strip()}') # this will provide the links for the jobs 


        print('\n') # this will print in the new lines 
