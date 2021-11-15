class Solution:
    def smallestSubsequence(self, text: str) -> str:
        count = collections.Counter(text)
        visited, stack = set(), []
        
        for ch in text:
            count[ch] -= 1
            if ch not in visited:
                # if stack[-1] > ch and stack[-1] will comes in later, we can remove it
                while stack and stack[-1] > ch and count[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(ch)
                visited.add(ch)
        
        return ''.join(stack)