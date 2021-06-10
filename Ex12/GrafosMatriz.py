import math

from Fila import Fila


class GrafosMatriz:
    grafo = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    estados = ["A", "B", "C", "D", "E", "F"]

    def ford(self, g, s, t):
        flow = 0
        anterior = []
        residuais = []
        fluxos = []

        for i in range(0, len(g)):
            anterior.insert(i, 0)

        while self.BFS(g, s, t, anterior):
            c = math.inf
            aux = t

            while aux != s:
                c = min(c, g[anterior[aux]][aux])
                aux = anterior[aux]

            flow += c
            j = t

            while j != s:
                i = anterior[j]
                g[i][j] -= c
                g[j][i] += c
                j = anterior[j]

            residuais.append(g)
            fluxos.append(flow)

        for i in range(0, len(residuais)-1):
            print(residuais[i])
            print("Fluxo", i + 1, ":", fluxos[i])

        print(residuais[len(residuais)-1])
        print("Fluxo Final", ":", fluxos[len(residuais)-1])


    def BFS(self, g, s, t, anterior):
        color = []
        distancia = []

        for i in range(0, len(g)):
            color.append("white")
            distancia.append(math.inf)

        color[s] = "gray"
        distancia[s] = 0
        anterior[s] = 0

        queue = Fila()
        queue.enqueue(s)

        while queue.size() != 0:
            u = queue.dequeue()

            for j in range(0, len(g[u])):
                if g[u][j] > 0 and color[j] == "white":
                    color[j] = "gray"
                    distancia[j] = distancia[u] + 1
                    anterior[j] = u
                    queue.enqueue(j)

            color[u] = "black"

        if color[t] == "black":
            return True
        else:
            return False
