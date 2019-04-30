class Solution:
    def climbStairs(self, n: int) -> int:
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