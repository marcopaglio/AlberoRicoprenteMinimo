from UnionFind import *
from GeneratoreGrafi import *


class Arrow:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def getFirst(self):
        return self.i

    def getSecond(self):
        return self.j

    def printArrow(self):
        print('(',self.getFirst(),',', self.getSecond(),')')


def algKruscal(G):
    A = []                                      ###insieme degli archi###
    unionFind = UnionFind()
    for i in range(G.numNodes):
        unionFind.makeSet(i)
    list = arcOrd(G.matrix)                     ###in uscita mi serve la lista degli archi ordinati###
    for i in list:
        if unionFind.findSet(i.getFirst()) != unionFind.findSet(i.getSecond()):
            unionFind.union(i.getFirst(), i.getSecond())
            A.append(i)
    return A

def arcOrd(matrix):
    list = {}
    for i in range(matrix.shape[0]):            ###shape[0] == numero righe
        for j in range(matrix.shape[1]):        ###shape[1] == numero colonne
            if matrix[i, j] != 0:
                list[Arrow(i,j)] = matrix[i, j]   ###inserisce in un dizionario tutti gli archi con peso non nullo###
    return dict(sorted(list.items(), key=lambda x: x[1]))     ###sorted fa tornare un array ordinato in senso decrescente rispetto al valore###

def showGraph(A, N):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    G.nodes()
    for i in A:
        G.add_edge(i.getFirst(), i.getSecond())
    G.edges()
    nx.draw(G, with_labels=True)
    plt.show()
