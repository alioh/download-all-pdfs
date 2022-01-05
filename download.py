import requests
import urllib.request
from bs4 import BeautifulSoup
  
# URL to download files from
url = requests.get('')

soup = BeautifulSoup(url.content,"lxml")

for a in soup.find_all('a', href=True):
    try:
        hrefs = a['href']
        if(hrefs[-4:]=='.pdf'):
            urllib.request.urlretrieve(a['href'], f"{a['href'].split('/')[-1].split('.')[0]}.pdf")
    except:
        continue