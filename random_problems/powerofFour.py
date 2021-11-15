class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return 1
        if n < 0 :
            return 0
        strN=bin(n)[2:] 

        if (strN.count('1') ==1) and(strN.count('0')%2==0):
            return 1
        else:
            return 0