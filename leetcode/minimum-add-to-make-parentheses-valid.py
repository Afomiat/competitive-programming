class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        temp = []
        l = 0

        while l < len(s):
            if s[l] == '(':
                stack.append(s[l])
                l += 1
            elif not stack and s[l] == ')':
                temp.append(s[l])
                l += 1
            elif stack and s[l] == ')':
                stack.pop()
                l += 1
        
        return len(stack) + len(temp)
