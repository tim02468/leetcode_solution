class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # mathematical solution
        numerator = 1
        for i in range(max(n-1, m-1), m + n - 2):
            numerator *= i + 1
        
        denominator = 1
        for i in range(min(n-1, m-1)):
            denominator *= i + 1    
        
        return int(numerator / denominator)
        
        board = [[1 for _ in range(m)] for _ in range(n)]
        
        # dp solution
        for i in range(1, n):
            for j in range(1, m):
                board[i][j] = board[i - 1][j] + board[i][j - 1]
        return board[-1][-1]