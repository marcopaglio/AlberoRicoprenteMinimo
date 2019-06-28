from UnionFind import *

def connectedComponents(G):
    unionFind = UnionFind()
    for k in range(G.numNodes):
        unionFind.makeSet(k)      ###creo nuovo insieme con valore k###
    for i in range(G.numNodes):
        for j in range(G.numNodes):
            if G.matrix[i, j] != 0:
                if unionFind.findSet(i) != unionFind.findSet(j):
                    unionFind.union(i, j)
    return unionFind