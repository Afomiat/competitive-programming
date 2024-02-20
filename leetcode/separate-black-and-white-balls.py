class Solution:
    def minimumSteps(self, s: str) -> int:
        
        swap, count_one = 0, 0

        for r in range(len(s)):
            if s[r] == '1':
                count_one += 1
            else:
                swap += count_one
        return swap