from collections import defaultdict
class DFS:
    def __init__(self,numv):
        self.adjlist = defaultdict(list)
        self.numv = numv
    
    def addedge(self,s,d):
        self.adjlist[s].append(d)

    def dfsutil(self,v,visited,recstack):
        visited[v] = True
        recstack[v] = True


        for i in self.adjlist[v]:
            if visited[i] == False:
               if self.dfsutil(i,visited,recstack):
                   return True
            elif recstack[i] == True:
                return True

        recstack[v] = False
        return False

    def dfs(self):
        visited = [False] * self.numv
        recstack = [False] * self.numv
        keys = list(self.adjlist.keys())

        for k in self.adjlist:
            if k not in visited:
                if self.dfsutil(k,visited,recstack):
                    return True
            
        return False

       
    
graph = DFS(4)
graph.addedge(3,0)
graph.addedge(1,3)
graph.addedge(2,1)
graph.addedge(0,2)
print(graph.dfs())