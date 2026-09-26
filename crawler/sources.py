import requests
from bs4 import BeautifulSoup
from collections import Counter


get_jobs_linkedIn='https://www.linkedin.com/jobs/search/?currentJobId=4471875975&origin=JOBS_HOME_JYMBII'


req=requests.get(get_jobs_linkedIn,auth=('gaurav-mahajan-6069b42b7','hetushma.12345'))

req.headers['content-type']='application/json'
soup=BeautifulSoup(req.content,'html.parser')

alljobswithoutduplicates=soup.find_all('a',class_='base-card__full-link')

print(len(alljobswithoutduplicates))
print(alljobswithoutduplicates)