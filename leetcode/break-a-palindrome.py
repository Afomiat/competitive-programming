class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
       
        p = list(palindrome)
        res = ''
        if len(p) == 1:
            return ''
        changed = False
        for i in range(len(p)//2):
            if p[i] != 'a':
                p[i] = 'a'
                changed = True
                break
       
        if not changed:
            p[-1] = 'b'
        res = ''.join(p)       
        return res