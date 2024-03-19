class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        l, r = 0, len(s)
        res = ''
        def checker(s):
            return True if len(set(s))// 2 == len(set(s.lower())) else False
        while r >= l:
            while l <= r:
                string = s[l:r]
                if checker(string):
                    if len(string) >= len(res):
                        res = string
                l += 1
            l = 0
            r -= 1
        return res
