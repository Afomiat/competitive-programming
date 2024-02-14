class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        l = 0
        swap = 0
        count_one = 0
        while l < len(s):
            if s[l]== '1':
                count_one += 1
                l += 1
          
            else:
                swap += count_one
                l += 1
              
        return swap