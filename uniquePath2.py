class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp solution
        # build board
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        # edge case
        if obstacleGrid[0][0] == 1:
            return 0
        
        # start point
        obstacleGrid[0][0] = 1
        
        # Filling the values for the first row
        for i in range(1, row):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first col        
        for j in range(1, col):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
                
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                
        return obstacleGrid[-1][-1]