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

    distancia = []

    anterior = []

    color = []

    arvore = []

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
        #print(queue.queue)

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

        #print(self.distancia)
        return self.arvore

    '''def dist(self, a, b):

        self.BFS(a)

        if b == a:
            print(a)

        else:

            if self.anterior[b] == None:

                print("Caminho não existe.")


            else:

                self.dist(a,self.anterior[b])

                print(b)'''

    def dist2(self, a, b):

        self.BFS(a)

        print(f"Distancia de {a} para {b}: ", self.distancia[b])

    def maxDist(self):

        maior = 0

        for i in range(0, len(self.estados)):

            self.BFS(i)

            for j in range(0, len(self.estados)):

                if self.distancia[j] >= maior:
                    maior = self.distancia[j]

            # maior = max(self.distancia)

        print(f"Diametro do grafo: {maior}")


    def media(self, s):

        soma = 0

        self.BFS(s)

        for i in range(0, len(self.distancia)):
            soma += self.distancia[i]

        media = soma / len(self.distancia) # - 1

        print(f"Distancia Media : {media}")
