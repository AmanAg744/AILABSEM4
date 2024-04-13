import heapq

def calcheuristic(start,goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

def get_neighbors(point, maze):
    neighbors = []
    r,c = point

    for cr,cc in [(1,0),(0,1),(-1,0),(0,-1)]:
        newr,newc = r + cr,c + cc
        if 0<=newr<len(maze) and 0<=newc<len(maze[0]) and maze[newr][newc] == 0:
            neighbors.append((newr,newc))
    
    return neighbors


def construct_path(came_From,curr):
    total_path = [(curr,0)]
    while curr in came_From:
        curr,cost = came_From[curr]
        total_path.append((curr,cost))

    return total_path[::-1]

def astar(maze,start, goal):
    openset = []
    heapq.heappush(openset,(0,start))
    came_from = {}
    g_score = {start:0}
    f_score = {start: calcheuristic(start,goal)}

    while openset:
        current_cost,current_node = heapq.heappop(openset)

        if current_node == goal:
            return construct_path(came_from,goal)
        
        for neighbor in get_neighbors(current_node, maze):
            tent_g_score = g_score[current_node] + 1

            if neighbor not in g_score or tent_g_score < g_score[neighbor]:
                
                g_score[neighbor] = tent_g_score
                f_score[neighbor] = g_score[neighbor] + calcheuristic(neighbor,goal)
                came_from[neighbor] = (current_node,calcheuristic(current_node,goal))
                heapq.heappush(openset,(f_score[neighbor],neighbor))


    return None










maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0,0)
goal = (4,4)

path = astar(maze,start,goal)
print(path)




