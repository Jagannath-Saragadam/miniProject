import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

urls = [line.rstrip('\n') for line in open('C:/Users/Jagannath/Desktop/mini project/mini-project/URL_test.txt')]

x=0
for url in urls:

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    soup=BeautifulSoup(page.read(),"html.parser")

    file=open("url_content"+str(x)+".txt",'w')

    for h1 in soup.find_all('h1'):
        file.writelines(h1.text)
    #for p in soup.find_all('p'):    
     #   file.writelines(p.text)
    
    x+=1
    file.close()
    
