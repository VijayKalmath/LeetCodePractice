# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 :
            return 2
        if n == 1 :
            return 1
        pi=1
        pj=2
        for i in range(n-2):
            output = pi + pj 
            pi = pj 
            pj = output 
        return output