class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i):
            num = ''
            alpha = ''

            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    num += s[i]
                elif s[i].isalpha():
                    alpha += s[i]
                elif s[i] == '[':
                    idx, st = helper(i + 1)
                    alpha += int(num) * st if num != '' else alpha + st
                   
                    num = ''
                    i = idx
                i += 1
            return (i, alpha)
        res = helper(0)
        return res[1]

       