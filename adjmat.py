class Graph:
    def __init__(self,numv):
        self.adjmat = [[0 for _ in range(numv)]for _ in range(numv)]
        self.numv = numv
        
    def add_edge(self,source,dest,weight):
        self.adjmat[source][dest] = weight
        
    

    def printadjlist(self):
        for i in range(self.numv):
            for j in range(self.numv):
                print(self.adjmat[i][j],end=" ")
            print("\n")


g = Graph(5)
g.add_edge(0,1,5)
g.add_edge(0,2,10)
g.add_edge(1,3,5)
g.add_edge(1,4,5)
g.add_edge(2,3,4)
g.add_edge(3,4,9)
g.add_edge(4,3,10)
g.printadjlist()