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

    grafo2 = [[0, 0, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0]]

    estados2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    vertices = []

    arvore = []

    pilha = Stack()

    componente = []

    componentes = []

    color = []

    def __init__(self):
        for i in range(0, len(self.estados2)):
            self.vertices.append(False)

    def stackDFS(self, u):
        self.arvore.clear()
        self.color.clear()

        self.pilha.add(u)

        for i in range(0, len(self.estados)):
            self.color.append("white")

        self.color[u] = 'gray'
        global noWay
        noWay = True

        while self.pilha.size() > 0:
            u = self.pilha.get()

            for i in range(0, len(self.grafo[u])):
                noWay = True
                if self.grafo[u][i] == 1:

                    if self.color[i] == 'white':
                        self.color[i] = 'gray'
                        self.pilha.add(i)
                        self.arvore.append([self.estados[u], self.estados[i]])
                        noWay = False
                        break

            if noWay:
                self.color[u] = 'black'
                self.pilha.remove()

        return self.arvore

    def recursiveDFS(self, u):
        self.vertices[u] = True
        self.componente.append(u)

        for i in range(0, len(self.grafo2[u])):
            if self.grafo2[u][i] == 1:
                if not self.vertices[i]:
                    self.recursiveDFS(i)
        return self.arvore

    def getComponents(self):
        for i in range(0, len(self.estados2)):
            if not self.vertices[i]:
                self.componente.clear()
                self.recursiveDFS(i)

                aux = []

                for j in range(0, len(self.componente)):
                    aux.append(self.estados2[self.componente[j]])

                self.componentes.append(aux)

    def checkConexos(self):
        self.getComponents()

        print("Quantidades de componentes conexos: ", len(self.componentes))

        for i in range(0, len(self.componentes)):
            print(f"Quantidade de vertice do componente {i + 1}: {len(self.componentes[i])}")

        for i in range(0, len(self.componentes)):
            print(f"Vertices do componente {i + 1}: ")

            for j in range(0, len(self.componentes[i])):
                print(f"{self.componentes[i][j]}", end=" ")

            print()

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

    def getTuplaConexo(self):
        x = []

        for i in range(0, len(self.grafo2)):
            for j in range(0, len(self.grafo2[0])):
                if self.grafo2[i][j] != 0:
                    x.append([i, j])

        for i in range(0, len(x)):
            for j in range(0, len(x[0])):
                x[i][j] = self.estados2[x[i][j]]

        return x
