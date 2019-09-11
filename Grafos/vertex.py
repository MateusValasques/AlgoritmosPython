class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addVizinho(self,nbr,weight=0):
        self.connectedTo[nbr] = weight    

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id


    def getWeight(self,nbr):
        return self.connectedTo[nbr]