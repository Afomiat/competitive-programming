class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = 0, n - k 
        tot = sum(cardPoints[r:])
        result = tot
        while r < n:
            tot += (cardPoints[l] - cardPoints[r])
            result = max(result, tot)
            l += 1
            r += 1
            
        return result