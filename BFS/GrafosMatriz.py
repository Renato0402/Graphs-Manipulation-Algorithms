import math
from Queue import Queue


class GrafosMatriz:
    grafo = [[0, 1, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 1, 1, 0],
             [0, 0, 1, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 1, 0],
             [0, 0, 1, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0, 1, 0]]

    estados = ["r", "s", "t", "u", "v", "w", "x", "y"]

    def BFS(self, s):
        color = []
        distancia = []
        anterior = []

        arvore = []

        for i in range(0, len(self.estados)):
            color.append("white")
            distancia.append(math.inf)
            anterior.append(None)

        color[s] = "gray"
        distancia[s] = 0
        anterior[s] = None

        queue = Queue()
        queue.enqueue(self.estados[s])
        print(queue.queue)

        while queue.size() != 0:
            u = queue.dequeue()
            u = self.estados.index(u)

            for j in range(0, len(self.grafo[u])):
                if self.grafo[u][j] == 1:
                    if color[j] == "white":
                        color[j] = "gray"
                        distancia[j] = distancia[u] + 1
                        anterior[j] = u
                        queue.enqueue(self.estados[j])

                        arvore.append([self.estados[u], self.estados[j]])

            color[u] = "black"
            print(queue.queue)

        return arvore