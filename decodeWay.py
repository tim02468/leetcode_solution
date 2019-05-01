class Solution:
    def numDecodings(self, s: str) -> int:
        # edge case
        if s[0] == '0':
            return 0
        
        # recursive solution with dp
        def decode(step, prev_step, n):   
            if step > n:
                return 0
               
            subString = s[prev_step:step]
            # step == 0 means first initial no substring
            if step != 0:
                if subString[0] == '0' or int(subString) > 26:
                    return 0

                if step == n:
                    return 1

            # memoize
            if memo[step] != -1:
                return memo[step]
            
            memo[step] = decode(step + 1, step, n) + decode(step + 2, step, n)
            
            return memo[step]
        
        memo = [-1 for _ in range(len(s))]
        return decode(0, 0, len(s))