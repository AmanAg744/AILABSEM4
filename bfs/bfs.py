from collections import defaultdict

class BFS:

    def __init__(self,numv):
        self.adjlist = defaultdict(list)
        self.numv = numv

    def addedge(self,s,d):
        self.adjlist[s].append(d)
    
    def bfs(self,s):
        visited = [False] * self.numv
        queue = [s]

        while queue:
            curr = queue.pop(0)
            print(curr,end=' ')
            
            for i in self.adjlist[curr]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

    
graph = BFS(4)
graph.addedge(4,1)
graph.addedge(4,2)
graph.addedge(2,3)
graph.addedge(1,3)
graph.bfs(4)

