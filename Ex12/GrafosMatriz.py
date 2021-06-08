import math

class GrafosMatriz:
    grafo = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    estados = ["A", "B", "C", "D", "E", "F"]
    d = []
    p = []
    minimo = 0
    v = []
    hasCaminho = True


    def ford(self, g, s,estados, d):
     somaFluxo = 0
     inc = 0

     while self.bellman(g, s, estados, d):
      u = s
      c = self.minimo
      somaFluxo+=c

      for i in range(len(self.v) - 1, -1, -1):
         g[u][self.v[i]] -= c
         g[self.v[i]][u] += c
         u = self.v[i]

      inc+=1
      print(g)
      print('Fluxo',inc,'=',somaFluxo)
      print('\n')
     print('Fluxo final:',somaFluxo)




    def initializeSS(self, grafo, s):
        for i in range(0, len(grafo)):
            self.d.insert(i, math.inf)
            self.p.insert(i, 0)

        self.d[s] = 0

    def relax(self, u, v, w):
        if self.d[u] + w[u][v] < self.d[v]:
            self.d[v] = self.d[u] + w[u][v]
            self.p[v] = u

    def bellman(self, grafo, s, estados,d):

        self.initializeSS(grafo, s)

        for _ in range(1, len(grafo) - 1):
            for i in range(0, len(grafo)):
                for j in range(0, len(grafo[i])):
                    if grafo[i][j] != 0:
                        self.relax(i, j, grafo)



        self.getPath( s,grafo,self.p, d, estados)

        return self.hasCaminho

    def getPath(self,src,grafo,  caminho, proximo, estados):


        global prox
        prox = proximo
        vAux = []

        global aux
        aux = src
        vAux2 = []

        while True:
            aux = caminho[prox]
            if aux != 0:
                vAux.append(prox)
                prox = caminho[prox]

            if aux == 0:
                vAux.append(prox)
                break

        for i in range(len(vAux) - 1, -1, -1):

           vAux2.append(grafo[aux][vAux[i]])

           if grafo[aux][vAux[i]]!= 0:
               self.hasCaminho = True
           else:
               self.hasCaminho = False

           aux = vAux[i]


        self.minimo = min(vAux2)

        self.v = vAux

