from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

file = open('sample.txt', 'r')
lines = file.readlines()

documents=lines
'''
documents = ['reads one line\n', 'pakistani poet mohammad iqbal\n', 'warns nawaz sharifin\n', 'pakistan independence day\n', '2017 file photo\n', 'pakistani poet mohammad iqbal\n', 'sent home without completing\n', 'hinduspokesman zabiullah mujahid says\n', 'advocate salman akram raja\n', 'filed three review petitions\n', '\xe2\x80\x98 unjust verdict \xe2\x80\x99\n', 'pakistan may face\n', 'military intelligence \xe2\x80\x94\n', 'judiciary \xe2\x80\x9d remarks\n', 'warns nawaz sharifin\n', '18 prime ministers\n', 'pakistan .\xe2\x80\x9c although\n', 'sent home ,\xe2\x80\x9d\n', 'muhammad safdar filed\n', 'panama papers scandal\n', 'panama papers investigation\n', 'nobel peace prize\n', 'national accountability bureau\n', 'must ensure respect\n', 'lawyers \xe2\x80\x99 convention\n', 'judges would supervise\n', 'joint investigation agency\n', 'intentionally never separated\n', 'http :// www\n', 'counsel khawaja haris\n', 'supreme court \xe2\x80\x99\n', 'national security ,\xe2\x80\x9d\n', 'intelligence agencies\n', 'pakistan independence day\n', 'petitioners also objected\n', 'july 28 decision\n', '2017 file photo\n', 'eventuality like\n', 'sharif \xe2\x80\x99\n', 'family challenged\n', 'court \xe2\x80\x99\n', '1971 following\n', '\xe2\x80\x9c anti\n', 'supreme court\n', 'another\n', 'sharif said\n', 'sent home without completing\n', 'hinduspokesman zabiullah mujahid says\n', 'advocate salman akram raja\n', 'filed three review petitions\n', '\xe2\x80\x98 unjust verdict \xe2\x80\x99\n', 'military intelligence \xe2\x80\x94\n', 'judiciary \xe2\x80\x9d remarks\n', 'pakistan may face\n', 'pakistan .\xe2\x80\x9c although\n', '18 prime ministers\n', 'sent home ,\xe2\x80\x9d\n', 'muhammad safdar filed\n', 'panama papers scandal\n', 'panama papers investigation\n', 'nobel peace prize\n', 'national accountability bureau\n', 'must ensure respect\n', 'lawyers \xe2\x80\x99 convention\n', 'judges would supervise\n', 'joint investigation agency\n', 'intentionally never separated\n', 'http :// www\n', 'counsel khawaja haris\n', 'supreme court \xe2\x80\x99\n', 'national security ,\xe2\x80\x9d\n', 'intelligence agencies\n', 'petitioners also objected\n', 'july 28 decision\n', 'eventuality like\n', 'family challenged\n', 'court \xe2\x80\x99\n', 'sharif \xe2\x80\x99\n', '\xe2\x80\x9c anti\n', 'supreme court\n', 'microsoft internet explorer 8\n', 'site best viewed\n', 'microsoft internet explorer 8\n', 'site best viewed\n', 'rights reserved ."\n', 'extra blank row every\n', '50 million developers come\n', 'writing code without\n', 'seriously bad duplication\n', 'problem also happened\n', 'largest developer community\n', 'simpler generic way\n', 'csv python module\n', 'breaks python 2\n', '5 months agoviewed9\n', 'extra blank row every\n', '50 million developers come\n', 'writing code without\n', 'seriously bad duplication\n', 'problem also happened\n', 'largest developer community\n', 'simpler generic way\n', 'csv python module\n', 'breaks python 2\n', '5 months agoviewed9\n', 'vivian l\xc3\xb3pez associate professor\n', 'data mining research group\n', 'moreno associate professor\n', 'natural language processing\n', 'http :// mida\n', 'geographical information systems\n', 'speech recognition ."\n', 'data mining\n', 'mar\xc3\xada n\n', 'widespread sexual harassment\n', 'tired old trope\n', 'old child prodigy\n', 'much pointless knowledge\n', 'harvey weinstein row\n', 'exemplary detective work\n', 'bound film reinvents\n', 'bollywood quiz master\n', '"" khamma ghani\n', '"" amit masurkar\n', '10 years old\n', '12 without playing\n', 'wait 25 years\n', 'could read newspapers\n', 'loopdjango linksthe web framework\n', 'level python web framework\n', 'build better web apps\n', 'encourages rapid development\n', 'help developers take applications\n', 'django takes security seriously\n', 'web leverage django \xe2\x80\x99\n', 'app without needing\n', 'mailing list documentation\n', '0 beta 1\n', 'upcoming django 2\n', 'loopdjango linksthe web framework\n', 'level python web framework\n', 'build better web apps\n', 'encourages rapid development\n', 'django software foundation\n', 'help developers take applications\n', 'django takes security seriously\n', 'web leverage django \xe2\x80\x99\n', 'app without needing\n', 'mailing list documentation\n', '0 beta 1\n', 'upcoming django 2\n', 'django software foundation ."\n', 'occasional dance partydinner parties\n', 'film festivalscasual happy hours\n', 'eventevent savedeventbrite uses cookies\n', 'time festivalsenlightening seminars\n', 'night celebrationsobstacle races\n', 'major music festivals\n', 'intimate house concerts\n', 'big gamebusiness mixers'] 
'''
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)


true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print ("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print (' %s' % terms[ind])
    print
