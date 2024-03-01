class Graph:
    def __init__(self):
        self.adjlist = {}
    def add_edge(self,source,dest,weight):
        if source not in self.adjlist:
            ls = {}
            ls[dest] = weight
            self.adjlist[source] = ls
        else:
            self.adjlist[source][dest] = weight

    def printadjlist(self):
        for i in self.adjlist:
            print(f"{i}->{self.adjlist[i]}")

g = Graph()
g.add_edge(0,1,5)
g.add_edge(0,2,10)
g.add_edge(1,3,5)
g.add_edge(1,4,5)
g.add_edge(2,3,4)
g.add_edge(3,4,9)
g.add_edge(4,3,10)
g.printadjlist()
            
