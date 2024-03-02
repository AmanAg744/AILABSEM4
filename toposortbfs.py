from collections import defaultdict
class graph:
    def __init__(self):
        self.adjlist = defaultdict(list)

    def addedge(self,s,d):
        self.adjlist[s].append(d)

    def toposort(self):
        indegree = {}
        for v in self.adjlist:
            indegree[v] = 0

        queue = []
        result = []

        for i in self.adjlist:
            for j in self.adjlist[i]:
                indegree[j] +=1

        for i in self.adjlist:
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            vert = queue.pop(0)
            result.append(vert)
            for i in self.adjlist[vert]:
                indegree[i] -=1
                if indegree[i] == 0:
                    queue.append(i)

        if len(result) != len(self.adjlist):
            print("cycle presnt ")
            return

        print(result)
        return

g = graph()
g.addedge('A','B')
g.addedge('A','C')
g.addedge('B','C')
g.addedge('B','F')
g.addedge('C','D')
g.addedge('D', 'E')
g.addedge('E','F')
g.addedge('F','D')
g.addedge('F','E')
g.toposort()