class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        st = ' '.join(result[::-1])
        
        return st