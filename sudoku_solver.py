class Sudk:
    def __init__(self):
        self.grid = [
            [0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 8, 0, 0, 0, 7, 0, 9, 0],
            [6, 0, 2, 0, 0, 0, 5, 0, 0],
            [0, 7, 0, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 4, 0],
            [0, 0, 5, 0, 0, 0, 6, 0, 3],
            [0, 9, 0, 4, 0, 0, 0, 7, 0],
            [0, 0, 6, 0, 0, 0, 0, 0, 0]
        ]

    def isvalid(self, r, c, k): 
        for i in range(9):
            if self.grid[r][i] == k or self.grid[i][c] == k:
                return False

        sr,sc = (r//3)*3,(c//3)*3
        for i in range(sr,sr+3):
            for j in range(sc,sc+3):
                if self.grid[i][j] == k:
                    return False
        return True
    
    def solve(self, r=0, c=0):
        if r == 9:
            return True
        elif c == 9:
            return self.solve(r+1, 0)
        elif self.grid[r][c] != 0:
            return self.solve(r, c+1)
        else:
            for k in range(1, 10):
                if self.isvalid(r, c, k):
                    self.grid[r][c] = k
                    if self.solve(r, c+1):
                        return True
                    else:
                        self.grid[r][c] = 0
            return False
        
    def showgrid(self):
        for row in self.grid:
            print(row)
        
sudoku = Sudk()
sudoku.solve()
sudoku.showgrid()
