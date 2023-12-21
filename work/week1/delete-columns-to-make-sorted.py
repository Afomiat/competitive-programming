class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        L_strs = list(zip(*strs))
        count = 0
        for s in L_strs:
            s = list(s)
            for i in range(len(s)):
                s[i] = ord(s[i])
            if s != sorted(s):
                count += 1
        return count