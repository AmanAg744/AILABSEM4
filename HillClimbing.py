#n queens



def calculateattacks(queens):
    n = len(queens)
    attack = 0
    for i in range(n):
        for j in range(i+1,n):
            if queens[i]==queens[j] or abs(queens[i] - queens[j]) == j-i:
                attack+=1
    
    return attack

def get_neighbors(queens):
    neighbors = []
    for i in range(len(queens)):
        for j in range(len(queens)):
            if j!=queens[i]:
                neighbor = queens.copy()
                neighbor[i] = j
                neighbors.append(neighbor)
        
    return neighbors

def nqueenshc(n,board):
    current_board = board
    current_attack = calculateattacks(current_board)
    while current_attack>0:
        neighbors = get_neighbors(current_board)
        next_board = min(neighbors,key=calculateattacks)
        next_attack = calculateattacks(next_board)
        if next_attack>=current_attack:
            break
        current_attack = next_attack
        current_board = next_board
    return current_board


def printboard(queens):
    for i in range(len(queens)):
        line = ""
        for j in range(len(queens)):
            if queens[j] == i:
                line+='1 '
            else:
                line+='0 '
        print(line)
    
n = 8
board = [1,3,5,7,2,4,6,0]


soln = nqueenshc(n,board)
printboard(soln)
print(soln)
    