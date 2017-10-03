import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup 
from rake_nltk import Rake  
import csv
#This part of the program opens the URLs scrapped from user browsing history(browser history.py)
with open("URL_test.txt","r") as f:
    content = f.readlines()

websites = [x.strip() for x in content] 

x=0
#Visits the website, saves the content(only text) of the website using beautifulsoup 4 into individual text files 
for website in websites:

    req = Request(website, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    soup=BeautifulSoup(page.read(),"html.parser")

    file=open("url_content"+str(x)+".txt",'w')

    for h1 in soup.find_all('h1'):
        file.writelines(h1.text)
    for p in soup.find_all('p'):    
        file.writelines(p.text)
    
    x+=1
    file.close()


#using RAKE (Rapid Automatic Keyword extraction using (3,0,0) parameters to extract the keywords from the scrapped website)
r=Rake()

file=open("url_content"+str(0)+".txt",'r')
myText=file.readlines()

for y in range(0,len(myText)): #error here 
    print(myText[y])
    print(r.extract_keywords_from_text(myText[y]))

#calculating the scores of each of the keyword (based on length and frequency of occurance)
scoredKeyowrds= r.get_ranked_phrases_with_scores()

#Calculating the mean of all the keywords
sum=0
for y in range(0,len(scoredKeyowrds)):
    sum=sum+scoredKeyowrds[y][0]

mean=sum/max(len(scoredKeyowrds),1)
#Creating a new list which contains only the keywords whose score is above the mean of all the scores
NewKeywords=[]
for y in range(0,len(scoredKeyowrds)):
    if scoredKeyowrds[y][0]>mean:
        NewKeywords.append(scoredKeyowrds[y])
    else:
        pass 

#Writing the new keywords into a file
f=open("Keywords.txt",'w')
for word in NewKeywords:
     f.write(','.join(str(s) for s in word) + '\n')


f.close()
#Converting the text file into a CSV file
with open ('Keywords.txt','r') as txt_file,open("KeywordsCSV.csv",'w') as csv_file :

    in_txt = csv.reader(txt_file, delimiter=",") 
    out_csv = csv.writer(csv_file)

    out_csv.writerows(in_txt)
