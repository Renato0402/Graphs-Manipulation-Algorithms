import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':

    x = nx.Graph()

    grafo = GrafosMatriz()

    '''x.add_edges_from(grafo.BFS(0))
    nx.draw_networkx(x)
    plt.show()'''

    #grafo.dist(1,7)

    grafo.dist2(0,6)

    grafo.maxDist()

    grafo.media(0)