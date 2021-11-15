class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alp_list = (re.findall(r'[a-zA-Z]',s))
        s = list(s)
        for i in range(len(s)):
            if ( (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122)) :
                s[i] = alp_list.pop()
        return ''.join(s)