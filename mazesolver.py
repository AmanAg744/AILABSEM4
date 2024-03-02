def dfs_maze(maze, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        row, col = stack.pop()
        result.append((row,col))   
        if (row, col) in visited:
            continue  

        visited.add((row, col))
         

        if maze[row][col] == 'E':
            result.append((row,col))
            return result  

        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and
                maze[new_row][new_col] != '1' and (new_row, new_col) not in visited): 
                stack.append((new_row, new_col)) 
                

    return None 


maze = [
    ['1', '1', '0', '1', '1'],
    ['0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '0', '0', '0', 'E'],
    ['1', '1', '1', '1', '1'],
]

start = (0, 2)

def main():
    solution = dfs_maze(maze, start)

    if solution:
       
        print(solution)

if __name__ == "__main__":
    main()