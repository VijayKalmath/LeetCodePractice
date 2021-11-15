class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True
        s_pointer = 0 
        for let in t :
            if let == s[s_pointer]:
                s_pointer +=1
            if s_pointer == len(s):
                return True
        return True if  s_pointer == len(s)  else False