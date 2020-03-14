import requests
import matplotlib.pyplot as plt

sites = ["http://www.netflix.com", "http://www.google.com", "http://www.facebook.com"] #server http
names = ["Netflix", "Google", "Facebook"]
plt.figure() #crea spazio per inserire grafico
massimo = 0 #massimo dei massimi

for (url,name) in zip(sites, names):
    print("Testing URL:", url)
    tempi = [] #vettore che contiene tempi di risposta per ogni sito
    for _ in range(10):
        R = requests.get('http://www.google.com') #richiesta get a Server in esame
        tempi.append(R.elapsed.microseconds/1000) #store del tempo di richiesta
    #stampo tempi di risposta minimo, massimo e medio per url in esame
    print("     Tempo di risposta minimo:", min(tempi), "ms")
    print("     Tempo di risposta massimo:", max(tempi), "ms")
    print("     Tempo di risposta medio:", sum(tempi)/len(tempi), "ms")
    plt.plot(tempi, label=name) #aggiungo valori di url in esame nel plot del grafico
    massimo = max([massimo, max(tempi)]) #ricalcolo massimo corrente
print("Il massimo dei massimi è: ", massimo) #stampo massimo dei massimi finale, massimo vlore tempo di richiesta tra i diversi url

plt.title("Confronto request.method = GET")
plt.ylim([0, 1.1*massimo]) #valori asse y da 0 a valore massimo
plt.xlim([0, len(tempi)]) #valori asse x da 0 a 10
plt.xlabel("ID richiesta") #labelx
plt.ylabel("Tempo di risposta [ms]") #labely
plt.legend(loc='lower right', fontsize=8) #legenda
plt.grid()
plt.show()
