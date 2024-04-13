from collections import defaultdict

class BFS:

    def __init__(self,numv):
        self.adjlist = defaultdict(list)
        self.numv = numv

    def addedge(self,s,d):
        self.adjlist[s].append(d)
    
    def bfs(self):
        indegree = [0] * self.numv
        queue = []
        result = []

        for i in self.adjlist:
            for j in self.adjlist[i]:
                indegree[j] += 1
        
        for i in self.adjlist:
            if indegree[i] == 0:
                queue.append(i)
       

        while queue:
            curr = queue.pop(0)
            result.append(curr)
            
            for i in self.adjlist[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(result)!= self.numv:
            print("Cyclic graph")
            return []
        return result

graph = BFS(4)
graph.addedge(3,0)
graph.addedge(3,1)
graph.addedge(1,2)
graph.addedge(0,2)
result = graph.bfs()
print(result)

