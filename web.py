import urllib.request
from bs4 import BeautifulSoup

page=urllib.request.urlopen('https://www.w3schools.com/js/js_json_intro.asp')

#print(page.read())
soup=BeautifulSoup(page.read(),"html.parser")

for p in soup.find_all('p'):
    print (p.text)
