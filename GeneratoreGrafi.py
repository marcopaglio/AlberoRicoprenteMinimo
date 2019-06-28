import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self, N, probability):
        self.numNodes = N
        self.matrix = np.zeros((N, N))
        if probability < 0:
            probability = 0
        elif probability > 100:
            probability = 100
        self.arrowGenerator(probability)

    def arrowGenerator(self, probability):
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                arrow = random.random() + (probability/100)
                if arrow >= 1:                                 ###di default è 0###
                    self.weightGenerator(i, j)

    def weightGenerator(self, i, j):
        weigth = int(random.random() * 100) + 1
        self.matrix[i,j] = weigth

    def getMatrix(self):
        return self.matrix

    def getNodes(self):
        return self.numNodes

    def showGraph(self):
        G = nx.Graph()
        G.add_nodes_from(range(self.numNodes))
        G.nodes()
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if self.matrix[i, j] != 0:
                    G.add_edge(i, j)
        G.edges()
        nx.draw(G, with_labels=True)
        plt.show()
