import heapq

def calcheuristic(start,goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

def get_neighbors(point,maze):
    neighbors = []
    x,y = point

    for cx,cy in [(1,0),(0,1),(-1,0),(0,-1)]:
        newx,newy = x + cx,y + cy
        if 0<=newx<len(maze) and 0<=newy<len(maze[0]) and maze[newx][newy] == 0:
            neighbors.append((newx,newy))

    return neighbors

def construct_path(camefrom, goal):
    total_path = [goal]
    while goal in camefrom:
        goal = camefrom[goal]
        total_path.append(goal)
    return total_path[::-1]
def astar(maze,start,goal):
    openset = []
    heapq.heappush(openset,(0,start))
    camefrom = {}
    g_score = {start:0}
    f_score = {start:calcheuristic(start,goal)}

    while openset:
        
        current_cost,current_node = heapq.heappop(openset)

        if current_node == goal:
            return construct_path(camefrom, current_node)
        

        for neighbor in get_neighbors(current_node,maze):
            tent_g_score = g_score[current_node] + 1
            if neighbor not in g_score or tent_g_score < g_score[neighbor]:
                camefrom[neighbor] = current_node
                g_score[neighbor] = tent_g_score
                f_score[neighbor] = g_score[neighbor] + calcheuristic(neighbor,goal)
                heapq.heappush(openset,(f_score[neighbor],neighbor))

    return None
    


maze = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (6, 6)
path = astar(maze,start,goal)
print(path)