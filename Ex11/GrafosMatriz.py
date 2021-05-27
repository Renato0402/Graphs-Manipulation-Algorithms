import math


class GrafosMatriz:
    grafo = [[0, 6, 7, 0, 0],
             [0, 0, 8, 5, 0],
             [0, 0, 0, -3, 9],
             [0, -2, 0, 0, 0],
             [0, 0, 0, 7, 0]]

    grafo1 = [[0, 4, 11],
              [6, 0, 2],
              [3, 0, 0]]

    grafo2 = [[0, 3, 8, 0, -4],
              [0, 0, 0, 1, 7],
              [0, 4, 0, 0, 0],
              [2, 0, -5, 0, 0],
              [0, 0, 0, 6, 0]]

    estados = ["s", "t", "x", "y", "z"]
    estados1 = ["1", "2", "3"]
    estados2 = ["1", "2", "3", "4", "5"]

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

    def floyd(self, grafo, estados):
        c = []
        p = []

        for i in range(0, len(grafo)):
            aux = []
            aux1 = []

            for j in range(0, len(grafo)):
                # aux1.insert(j, None)

                if grafo[i][j] != 0:
                    aux.insert(j, grafo[i][j])
                    aux1.insert(j, int(estados[i]))
                if grafo[i][j] == 0 and i != j:
                    aux.insert(j, math.inf)
                    aux1.insert(j, None)
                if i == j:
                    aux.insert(j, 0)
                    aux1.insert(j, None)

            c.insert(i, aux)
            p.insert(i, aux1)

        # print(c)
        print(p)

        for k in range(0, len(grafo)):
            for i in range(0, len(grafo)):
                for j in range(0, len(grafo)):
                    if c[i][j] > c[i][k] + c[k][j]:
                        c[i][j] = c[i][k] + c[k][j]

                        if p[k][j] is not None:
                            p[i][j] = p[k][j]
                        #if p[k][j] is None:
                            #p[i][j] = int(estados[p[k][j]])

                    # c[i][j] = min(c[i][j], c[i][k]+c[k][j])
            # print(c)
            print(p)
