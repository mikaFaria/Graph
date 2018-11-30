class graphVertex(object):
    def __init__(self):
        self.begin = None
        self.end = None
        self.weight = 0

    def isPathHelpDFS(self,endVertex,visited,path):
        if self.begin is not None:
            path.append(self.begin.value)
            if self.begin.vert.__contains__(endVertex):
                return path
            else:
                for i in range(self.begin.vert.__len__()):
                    if self.begin.vert[i] is not None and visited.__contains__(self.begin.vert[i]) == False:
                        visited.append(self.begin.vert[i])
                        return self.begin.vert[i].isPathHelpDFS(endVertex,visited,path)
        if self.end is not None:
            path.append(self.end.value)
            if self.end.vert.__contains__(endVertex):
                return path
            else:
                for i in range(self.end.vert.__len__()):
                    if self.end.vert[i] is not None and visited.__contains__(self.end.vert[i]) == False:
                        visited.append(self.end.vert[i])
                        return self.end.vert[i].isPathHelpDFS(endVertex,visited,path)
        return False

    def isPathHelpBFS(self,endVertex,visited):
        if self.begin is not None:
            if self.begin.vert.__contains__(endVertex):
                return True
        if self.end is not None:
            if self.end.vert.__contains__(endVertex):
                return True
            else:
                for i in range(self.end.vert.__len__()):
                    if self.end.vert[i] is not None and visited.__contains__(self.end.vert[i]) == False:
                        visited.append(self.end.vert[i])
                        return self.end.vert[i].isPathHelpBFS(endVertex,visited)
        if self.begin is not None:
            for i in range(self.begin.vert.__len__()):
                if self.begin.vert[i] is not None and visited.__contains__(self.begin.vert[i]) == False:
                    visited.append(self.begin.vert[i])
                    return self.begin.vert[i].isPathHelpBFS(endVertex, visited)

    def isPathDFS(self,endVertex):
        visited = []
        path = []
        return self.isPathHelpDFS(endVertex,visited,path)

    def isPathBFS(self,endVertex):
        visited = []
        return self.isPathHelpBFS(endVertex,visited)


class graphEdge(object):
    def __init__(self,value):
        self.value = value
        self.vert = []
        self.weight = -1 # Stands for Infinite

    def signVertex(self,vertex,endEdge,weight):
        vertex.begin = self
        vertex.end = endEdge
        vertex.weight = weight
        self.vert.append(vertex)
        endEdge.vert.append(vertex)

    def dijkstra(self,endEdge,visited):
        visited.append(self)
        if self is not None:
            self.weight = 0
            currEdgeW = self.weight
            minVertex = None
            for i in range(self.vert.__len__()):
                if self.vert[i].begin is self:
                    if self.vert[i].end == endEdge:
                        visited.append(self.vert[i].end)
                        return visited
                    currVertexW = self.vert[i].weight
                    self.vert[i].end.weight = currEdgeW + currVertexW
                    #print (self.vert[i].weight)
                    if minVertex == None:
                        minVertex = self.vert[i]
                    if self.vert[i].weight < minVertex.weight:
                        minVertex = self.vert[i]
                else:
                    if self.vert[i].begin == endEdge:
                        visited.append(self.vert[i].begin)
                        return visited
                    currVertexW = self.vert[i].weight
                    self.vert[i].begin.weight = currEdgeW + currVertexW
                    if minVertex == None:
                        minVertex = self.vert[i]
                    if self.vert[i].weight < minVertex.weight:
                        minVertex = self.vert[i]
            if minVertex.begin is not None:
                if minVertex.begin is self:
                    visited = minVertex.end.dijkstra(endEdge,visited)
            if minVertex.end is not None:
                if minVertex.end is self:
                    visited = minVertex.begin.dijkstra(endEdge,visited)
        return visited


def isConnected(vertexList):
    for i in range(vertexList.__len__()):
        for u in range(i+1,vertexList.__len__()):
            com = vertexList[i].isPathDFS(vertexList[u])
            if com == False:
                return False
    return True

VertexList = []

EdgeA = graphEdge(1)
EdgeB = graphEdge(2)
EdgeC = graphEdge(3)
EdgeD = graphEdge(4)
Edge5 = graphEdge(5)
Vertex1 = graphVertex()
EdgeA.signVertex(Vertex1,EdgeB,11)

VertexList.append(Vertex1)

Vertex2 = graphVertex()
EdgeA.signVertex(Vertex2,EdgeC,10)

VertexList.append(Vertex2)

Vertex3 = graphVertex()
Vertex4 = graphVertex()
Vertex5 = graphVertex()
Vertex6 = graphVertex()
EdgeA.signVertex(Vertex3,EdgeD,1)
EdgeB.signVertex(Vertex4,EdgeD,3)
EdgeC.signVertex(Vertex5,EdgeD,7)
EdgeD.signVertex(Vertex6,Edge5,10)


VertexList.append(Vertex3)
VertexList.append(Vertex4)
VertexList.append(Vertex5)
VertexList.append(Vertex6)

file=open("PathDFS.txt","w")
data = Vertex1.isPathDFS(Vertex6)
if data is not False:
    for edge in data:
        file.write(str(edge) + ',')


print ("")
print (isConnected(VertexList))
print ("")
visited = []

for ed in EdgeA.dijkstra(Edge5,visited):
    print (str(ed.value))
