import math


class GrafosMatriz:
    grafo = [[0, 6, 0, 7, 0],
             [0, 0, 5, 8, -4],
             [0, -2, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

    grafo2 = [[0, 5, 7, 1, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0],
              [0, 0, 0, 6, 5, 0, 0],
              [0, 3, 0, 0, 0, 5, 3],
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

    estados2 = ["a", "b", "c", "d", "e", "f", "g"]
    estados3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

    d = []
    p = []

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

    def initializeSS(self, grafo, s):
        for i in range(0, len(grafo)):
            self.d.insert(i, math.inf)
            self.p.insert(i, None)

        self.d[s] = 0

    def relax(self, u, v, w):
        if self.d[v] > self.d[u] + w[u][v]:
            self.d[v] = self.d[u] + w[u][v]
            self.p[v] = u

    def bellman(self, grafo, s):
        self.initializeSS(grafo, s)

        for i in range(0, len(grafo)):
            for j in range(0, len(grafo[i])):
                if grafo[i][j] != 0:
                    self.relax(i, j, grafo)

        for i in range(0, len(grafo)):
            for j in range(0, len(grafo[i])):
                if self.d[j] > self.d[i] + grafo[i][j]:
                    print(self.d)
                    return False

        print(self.d)
        return True
