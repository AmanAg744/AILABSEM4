class Sudk:
    def __init__(self):
        self.grid = [[1,0,0],
                     [0,2,0],
                     [0,0,3]]
    def isvalid(self,r,c,k):
        for i in range(3):
            if self.grid[r][i] == k or self.grid[i][c] == k:
                return False
        return True
    def solve(self,r=0,c=0):
        if r == 3:
            return True
        elif c == 3:
            return self.solve(r+1,0)
        elif self.grid[r][c] != 0 :
            return self.solve(r,c+1)
        else:
            for k in range(1,4):
                if self.isvalid(r,c,k):
                    self.grid[r][c] = k
                    if self.solve(r,c+1):
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

 