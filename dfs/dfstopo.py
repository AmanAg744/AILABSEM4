from collections import defaultdict
class DFS:
    def __init__(self,numv):
        self.adjlist = defaultdict(list)
        self.numv = numv
    
    def addedge(self,s,d):
        self.adjlist[s].append(d)

    def dfsutil(self,v,visited,stack):
        visited.add(v)

        for i in self.adjlist[v]:
            if i not in visited:
                self.dfsutil(i,visited,stack)

        stack.append(v)

    def dfs(self):
        visited = set()
        stack = []
        keys = list(self.adjlist.keys())

        for k in keys:
            if k not in visited:
                self.dfsutil(k,visited,stack)

        print(stack[::-1])
    
graph = DFS(4)
graph.addedge(4,1)
graph.addedge(4,2)
graph.addedge(2,3)
graph.addedge(1,3)
graph.dfs()