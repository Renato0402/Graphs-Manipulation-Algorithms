import networkx as nx
import matplotlib.pyplot as plt

from GrafosMatriz import GrafosMatriz

if __name__ == '__main__':
    #x = nx.Graph()

    grafos = GrafosMatriz()

    '''x.add_edges_from(grafos.getTupla())
    nx.draw_networkx(x)
    plt.show()'''

    grafos.dijkstra(grafos.grafo,grafos.estados,4)
