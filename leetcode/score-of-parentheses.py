class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        tamp = []
        stack = []
        count, res = 0, 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
                if s[i - 1] == '(':
                    res += 2 ** count

        return res