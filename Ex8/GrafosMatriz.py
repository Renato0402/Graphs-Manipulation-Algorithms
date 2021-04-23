import math

from Queue import Queue
from Stack import Stack

class GrafosMatriz:

    grafo = [[0, 0, 1, 1, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0],
             [1, 1, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 0, 1, 0],
             [0, 0, 0, 1, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0]]

    estados = ["1", "2", "3", "4", "5", "6", "7", "8"]

    vertices = []

    arvore = []

    distancia = []

    anterior = []

    color = []

    pilha = Stack()

    def __init__(self):
        for i in range(0, len(self.estados)):
            self.vertices.append(False)

    def DFS(self, u):

        self.arvore.clear()

        self.pilha.add(u)

        while self.pilha.size() > 0:

            u = self.pilha.remove()

            if not self.vertices[u]:

                self.vertices[u] = True

                for i in range(0, len(self.grafo[u])):

                    if self.grafo[u][i] == 1:

                        if not self.vertices[i]:

                            #self.DFS(i)
                            self.pilha.add(i)
                            self.arvore.append([self.estados[u], self.estados[i]])

        return self.arvore

    def BFS(self, s):

        self.distancia.clear()

        self.anterior.clear()

        self.color.clear()

        self.arvore.clear()

        for i in range(0, len(self.estados)):
            self.color.append("white")
            self.distancia.append(math.inf)
            self.anterior.append(None)

        self.color[s] = "gray"
        self.distancia[s] = 0
        self.anterior[s] = None

        queue = Queue()
        queue.enqueue(self.estados[s])
        print(queue.queue)

        while queue.size() != 0:
            u = queue.dequeue()
            u = self.estados.index(u)

            for j in range(0, len(self.grafo[u])):
                if self.grafo[u][j] == 1:
                    if self.color[j] == "white":
                        self.color[j] = "gray"
                        self.distancia[j] = self.distancia[u] + 1
                        self.anterior[j] = u
                        queue.enqueue(self.estados[j])

                        self.arvore.append([self.estados[u], self.estados[j]])

            self.color[u] = "black"
            # print(queue.queue)

        print(self.distancia)
        return self.arvore

    def checkConexo(self):

        for i in range(0, len(self.estados)):

            self.BFS(i)

            for j in range(0, len(self.estados)):

                if self.distancia[j] == 0:
                    return "Grafo é Desconexo"

        return "Grafo é Conexo"


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
