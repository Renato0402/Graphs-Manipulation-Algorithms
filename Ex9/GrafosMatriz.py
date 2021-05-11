import math


class GrafosMatriz:
    grafo = [[0, 2, 5, 1, 0, 0],
             [2, 0, 3, 2, 0, 0],
             [5, 3, 0, 3, 1, 5],
             [1, 2, 3, 0, 1, 0],
             [0, 0, 1, 1, 0, 2],
             [0, 0, 5, 0, 2, 0]]

    grafo2 = [[0, 5, 7, 1, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0],
              [0, 0, 0, 6, 5, 0, 0],
              [0, 0, 0, 0, 0, 5, 3],
              [0, 0, 0, 0, 0, 4, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0]]

    grafo3 = [[0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 0, 2, 0, 0],
              [0, 0, 11, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 3, 0, 3, 5, 0, 0, 6, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 4, 0],
              [0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
              [0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 8, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0]]

    estados = ["u", "v", "w", "x", "y", "z"]
    estados2 = ["a", "b", "c", "d", "e", "f", "g"]
    estados3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

    vertices = []

    arvore = []

    def __init__(self):
        for i in range(0, len(self.estados2)):
            self.vertices.append(False)

    def dijkstra(self, u):

        custo = []

        N = [u]

        for i in range(0, len(self.grafo[u])):

            if self.grafo[u][i] != 0:
                custo[i] = self.grafo[u][i]

            else:
                custo[i] = math.inf

        while len(N) != len(self.grafo[u]):
            # CONTINUAR

            pass


    def getTupla(self):
        x = []

        for i in range(0, len(self.grafo)):
            for j in range(0, len(self.grafo[0])):
                if self.grafo[i][j] != 0:
                    x.append([i, j])

        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                x[i][j] = self.estados[x[i][j]]

        return x
