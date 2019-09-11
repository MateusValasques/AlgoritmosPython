import numpy as np
from queue import Queue
from collections import defaultdict
from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}

    def addVertex(self, key):
        vertice = Vertex(key)
        self.vertList[key] = vertice

    def getVertex(self, key):
       return self.vertList[key] 

    def addEdge(self, f, t, cost=0):

        if not f in self.vertList:
            self.addVertex(self, f)

        if not t in self.vertList:
            self.addVertex(self, t) 

        self.getVertex(self, f).addVizinho(self, t, cost)

    #def getEdges(self):
    def getVertices(self):
        
   
        
    #def bfs(self, start):

    #def dfs(self, start):

    #def dijkstra(self, start, maxD=1e309):


if __name__ == "__main__":