class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True

        pal = ''
       
        for i in s:
            if i.isalnum():
                pal += i.lower()
        
        l, r = 0, len(pal) - 1
        while l < r:
            if pal[l] != pal[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

