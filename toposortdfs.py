from collections import defaultdict
class graph:
    def __init__(self):
        self.adjlist = defaultdict(list)
    def addedge(self,source,dest):
        # if source not in self.adjlist:
        #     ls = []
        #     ls.append(dest)
        #     self.adjlist[source] = ls
        # else:
            self.adjlist[source].append(dest)
    
    def dfs(self,vertex,stack,visited):
        visited.add(vertex)
        for i in self.adjlist[vertex]:
            if i not in visited:
                self.dfs(i,stack,visited)
        
        stack.append(vertex)

    def toposort(self):
        stack = []
        visited = set()
        keys = list(self.adjlist.keys())

        for i in keys:
            if i not in visited:
                self.dfs(i,stack,visited)
        
        print("Topo sorted : \n")
        print(stack[::-1])


g = graph()
g.addedge('A','B')
g.addedge('A','C')
g.addedge('B','C')
g.addedge('B','F')
g.addedge('C','D')
# g.addedge('D', 'E')
# g.addedge('E','D')
g.addedge('F','D')
g.addedge('F','E')
g.addedge('G','B')
g.addedge('G','F')
g.toposort()