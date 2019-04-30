class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        # check edge case
        if row == 1 and col == 1:
            return grid[0][0]
        
        # first row summantion
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
        
        # first col summantion
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        
        for r in range(1, row):
            for c in range(1, col):
                # check min previous path and add:
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])

        return grid[-1][-1]