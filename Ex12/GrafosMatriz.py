import math


class GrafosMatriz:
    grafo = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    estados = ["A", "B", "C", "D", "E", "F"]

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

    def ford(self, g, s, t):
        f = []

        for i in range(0, len(g)):
            f.insert(i, [])

            for j in range(0, len(g[i])):
                f[i].insert(j, 0)

        print(f)

        while self.hasCaminho(g, s, t):


    def hasCaminho(self, g, s, t):
        if self.grafo[s][t] != 0:
            return True
        else:
            return False

    def recursiveDFS(self, u):
        self.vertices[u] = True
        self.componente.append(u)

        for i in range(0, len(self.grafo2[u])):
            if self.grafo2[u][i] == 1:
                if not self.vertices[i]:
                    self.recursiveDFS(i)
        return self.arvore
