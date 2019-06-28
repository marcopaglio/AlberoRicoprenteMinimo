from algKruscal import *
from ComponentiConnesse import connectedComponents
from timeit import default_timer as timer
from decimal import *
import pickle

getcontext().prec = 4

###PROGRAMMA CHE CREA GRAFI DI DIMENSIONE E PROBABILITà DI ARCHI CRESCENTI###

N = 6                                    #fino a 63 nodi
prob = 10
recCC = {}
recMST = {}

recGraph = {}

while(prob < 75):
    #creazione grafo
    g = Grafo(N, prob)                    #crea grafo di N elementi con probabilità di archi del prob%
    print(g.getMatrix())                  #stampo la matrice di incidenza
    print('crea grafo di ',N,'elementi con probabilità di archi del ', prob, '%.')
    g.showGraph()                         #mostro il grafico creato

    #calcolo componenti connesse
    for i in range(5):
        start = Decimal(timer())
        unionFind = connectedComponents(g)    #creo le liste di nodi connessi e li memorizzo in uno unionFind
        end = Decimal(timer())
        print('Sono necessari ', end - start,' secondi per determinare le componenti di connesse di un grafo con ', N,' nodi e probabilità ', prob,'.')
        recCC[N] += end - start
    recCC[N] = recCC[N]/5
    unionFind.printUnionFind()            #stampo le liste di nodi connessi

    #calcolo MST
    for i in range(5):
        start = Decimal(timer())
        A = algKruscal(g)                     #creo MST
        end = Decimal(timer())
        print('Sono necessari ', end - start, ' secondi per determinare il MST di un grafo con ', N,' nodi e probabilità ', prob,'.')
        recMST[N] += end - start
    recMST[N] = recMST[N]/5
    #anzichè mostrare gli alberi qui, li mostro tutti alla fine perchè rallentano troppo l'esecuzione
    recGraph[N] = A
    for i in A:
        i.printArrow()                    #stampo gli archi usati nell'MST

    #aggiornamento dei valori
    N += int(N/4)
    prob += (100 - prob)/10

pickle.dump(recCC, open("CCTime.p", "wb"))          #creo file pickle dove inserire tempi CC
pickle.dump(recMST, open("MSTTime.p", "wb"))        #creo file pickle dove inserire tempi MST

print(':>Componenti Connesse ', recCC)
print(':> MST ', recMST)

#grafico andamento
plt.plot(recCC.keys(), recCC.values())
plt.plot(recMST.keys(), recMST.values())
plt.xlabel('dimensione, probabilità')
plt.ylabel('tempo')
plt.title('Componenti Connesse & Albero di Connessione Minimo')
plt.legend(['CC', 'MST'])
plt.show()

N = 6
for i in recGraph:
    showGraph(recGraph[N], N)  # mostro l'MST
    N += int(N/4)