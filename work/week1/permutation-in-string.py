class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        n = len(s2)
        m = len(s1)
        count_s2 = Counter(s2[:m])
        l = 0
        
        for r in range(n):
            if count_s1 == count_s2:
                return True
            if r + m < n:
                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]
                count_s2[s2[r + m]] += 1
                l += 1
        return False