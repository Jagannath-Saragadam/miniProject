from rake_nltk import Rake  

r=Rake()

myText="Wiki Loves Earth is an international photographic competition to promote natural heritage sites around the world through Wikimedia projects (mainly Wikipedia and Wikimedia Commons). Everybody can participate. There are a lot of natural heritage sites in India. The goal of Wiki Loves Earth is to encourage people to take pictures of those natural sites, and to put them under a free licence so that others may access them through the Internet. To achieve that, an international contest will take place from 01 June 2017 to 30 June 2017. This page introduces the Indian part of this competition.In June, you may upload as many pictures as you want of natural sites that you have visited. Pictures don't have to be taken in June, but must be uploaded during that month to be considered. Provide your photo with {{Wiki Loves Earth 2017|in}} template. At the end of the month, the contest jury will begin evaluating the photographs and will choose the best 10 pictures of the natural sites in India, and ultimately in the world.The full WLE rules can be read at Commons:Wiki Loves Earth 2017/Rules. In short the rules are:All protected or listed areas along with its natural Flora or Fauna in India are within the scope of this competition.For further queries you may write us at wikilovesearthindia@gmail.com"

r.extract_keywords_from_text(myText)

keywords=r.get_ranked_phrases()

scoredKeyowrds= r.get_ranked_phrases_with_scores()
#print (keywords)

print(scoredKeyowrds)