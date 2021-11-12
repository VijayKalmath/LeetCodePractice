class Solution:
    def fib(self, n: int) -> int:
        if n < 2: 
            return n 
        pi=0
        pj=1
        for i in range(n-1):
            output = pi + pj 
            pi = pj 
            pj = output 
        return output