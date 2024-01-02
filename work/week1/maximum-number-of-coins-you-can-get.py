class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        piles.sort(reverse=True)
        if len(piles) == 3:
            return piles[1]
        else:
            m = len(piles) // 3
            for i in range(1, len(piles) - m, 2):
                result += piles[i]
            return result
