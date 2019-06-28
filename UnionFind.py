from LinkedList import *

class UnionFind():
    def __init__(self):
        self.collection = []     ###insieme di insiemi (liste linkate) della union-find###
        self.delegates = {}      ####per avere i rappresentatnti delle liste a tempo costante li tengo in memeoria###
                                 ###...l'utlizzo di un dizionario non permette di avere nodi con chiave non numerica###

    def makeSet(self, x):
        temp = LinkedList() #crea la lista
        temp.add(x)         #aggiunge il valore
        self.collection.append(temp) #aggiunge la lista allo unionfind
        self.delegates[x] = x                   ###utilizzo di nodi ad indici naturali e crescenti###

    def findSet(self, x):
        return self.delegates[x]

    def union(self, x, y):
        xList = self.findList(x)         #costo proporzionale al numero di liste
        yList = self.findList(y)         #costo proporzionale al numero di liste
        if xList.size() >= yList.size(): #euristica dell'unione pesata
            self.aggregation(xList, yList)
            self.collection.remove(yList)
        else:
            self.aggregation(yList, xList)
            self.collection.remove(xList)


    def findList(self, x):
        delegate = self.findSet(x)
        count = 0
        current = self.collection[count]
        #è scontato che ci sia l'elemento richiesto
        while current.getDelegate() != delegate:
            count += 1
            current = self.collection[count]
        return self.collection[count]

    def aggregation(self, listIncreased, listDecreased):
        newDelegate = listIncreased.getDelegate()
        current = listDecreased.getHead()
        while current is not None:
            newNode = current.getData()
            listIncreased.add(newNode)                ###il rappresentante è aggiornato anche nella lista###
            self.delegates[newNode] = newDelegate     ###aggiorno il rappresentante###
            current = current.getNext()
        listDecreased.clear()                         ###pulisco la lista (elimino puntatori)###

    def printUnionFind(self):
        count = 1
        for i in self.collection:
            print('List number ', count)
            i.printList()
            count += 1



