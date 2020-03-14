import requests

sites = ["http://www.twitter.com ", "http://www.google.com", "http://www.youtube.com ", "http://www.polimi.it ", "http://www.wikipedia.org", "http://www.amazon.com "] #server http
names = ["Twitter", "Google", "YouTube", "Polimi", "Wikipedia", "Amazon"]
avg_tempi = []

for (url,name) in zip(sites,names): #scorro sia url che nome dei siti
    print("Testing URL:", url)
    tempi = [] #vettore che contiene tempi di risposta per ogni sito
    for _ in range(10):
        R = requests.get('http://www.google.com') #richiesta get a Server in esame
        tempi.append(R.elapsed.microseconds/1000) #store del tempo di richiesta
    T = sum(tempi)/len(tempi) #calcolo average
    avg_tempi.append(T) #aggiungo average a lista
    print("     Tempo di risposta medio:", int(T), "ms") #stampo tempo di risposta medio per ogni server

#stampo il miglior tempo di risposta medio e a che server si riferisce
print("Il tempo migliore di risposta media è : ", int(min(avg_tempi)), "ms di", names[avg_tempi.index(min(avg_tempi))])