import math
import matplotlib.pyplot as plt #adiciona os pontos para formar o grafico#
from matplotlib.widgets import Cursor, Button #importa as funcoes do cursor do mouse
import sys
import re
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button
import sys
import re

import numpy as np
from queue import Queue
from collections import defaultdict
from vertex import Vertex

#from Grafos.plot_pontos_silas import onclick


class Graph:

    def __init__(self):
        self.vertList = {}
        self.c1 = None
        self.c2 = None
        self.flip = True

    def addVertex(self, id, lat, lon):
        vertice = Vertex(id, lat, lon)
        self.vertList[id] = vertice

    def getVertex(self, key):
       return self.vertList[key] 

    def addEdge(self, f, t, cost=0):

        self.getVertex(f).addVizinho(t, cost)

    def haversine(self, lat1, lon1, lat2, lon2):

        # distance between latitudes
        # and longitudes
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0

        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0

        a = (pow(math.sin(dLat / 2), 2) +
             pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c

    def createAllVertex (self):
        with open("arquivo_teste") as fp:
            for line in fp:
                nos = line.split(" ")
                self.addVertex(nos[0], nos[1], nos[2])

    def createAllEdges (self):
        with open("arquivoadjlist") as fp:
            for line in fp:
                line = line.replace("\n", "")
                nos = line.split(" ")
                no_atual = nos[0]

                for i in range(1, len(nos)):

                    self.addEdge(no_atual, nos[i], self.haversine(float(self.getVertex(no_atual).lat), float(self.getVertex(no_atual).lon), float(self.getVertex(nos[i]).lat), float(self.getVertex(nos[i]).lon)))


    #def busca_largura(self):

    def busca_profundidade(self, vertice, visitados):
        visitados.add(vertice)
        for vizinho in self[vertice]:
            if vizinho not in visitados:
                self.busca_profundidade(self, vizinho, visitados)

    def djikstra(self, origem,fim):

            controle = {}
            distanciaAtual = {}
            noAtual = {}
            naoVisitados = []
            atual = origem
            noAtual[atual] = 0

            for vertice in self.keys():
                naoVisitados.append(vertice)
                distanciaAtual[vertice] = float('inf')

            distanciaAtual[atual] = [0, origem]

            naoVisitados.remove(atual)

            while naoVisitados:
                for vizinho, peso in self[atual].items():
                    pesoCalc = peso + noAtual[atual]
                    if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                        distanciaAtual[vizinho] = [pesoCalc, atual]
                        controle[vizinho] = pesoCalc

                if controle == {}: break
                minVizinho = min(controle.items(), key=lambda x: x[1])
                atual = minVizinho[0]
                noAtual[atual] = minVizinho[1]
                naoVisitados.remove(atual)
                del controle[atual]

            return distanciaAtual[fim][0]

    def main(self):

        self.createAllVertex()
        self.createAllEdges()
        #Criar o grafico
        file_name = "map.osm.txt"
        x = list()
        y = list()
        with open(file_name) as fp:
            for line in fp:
                points = re.findall(r'[-+]?\d+.\d+', line)
                x.append(float(points[1]))
                y.append(float(points[2]))
        #print(points)
        #plt.plot(x, y, 'ro')

        fig, ax = plt.subplots()

        p, = plt.plot(x, y, 'o')

        cursor = Cursor(ax,
                        horizOn=True,
                        vertOn=True,
                        color='green',
                        linewidth=2.0)



        c1 = fig.canvas.mpl_connect('button_press_event', self.onclick)
        print(c1)
        plt.show()

    def onclick(self, event):
        if self.flip:
            self.c1 = (event.xdata, event.ydata)
        else:
            self.c2 = (event.xdata, event.ydata)
        self.flip = not self.flip
        #x1, y1 = (event.xdata, event.ydata)

        #a magia tem que acontecer aqui
        print (self.c1, self.c2)


if __name__ == "__main__":
    g = Graph()
    g.main()


