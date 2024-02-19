class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in myMap:
                if stack and stack[-1]==myMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False