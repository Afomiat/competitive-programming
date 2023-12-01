class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            x= str(x)
            rev = x[::-1]
            if x == rev:
                return True
    
     
