class Solution:
    def climbStairs(self, n: int) -> int:
        # dp solution
        if n == 1:
            return 1
        
        # initial dp array
        dp = [0 for _ in range(n)]
        
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
        
        
        # dp by memoize method
        def climb(step, n):
            if step > n:
                return 0
            if step == n:
                return 1
            if step in memo:
                return memo[step]
            
            memo[step] = climb(step + 1, n) + climb(step + 2, n)
            return memo[step]
        
        memo = {}
        return climb(0, n)
