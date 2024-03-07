class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = 1
        max_val = max(piles) 
        ans = 0
        
        def helper(mid):
            cur = 0
            for i in piles:
                if mid >= i:
                    cur += 1
                else:
                    cur += math.ceil(i / mid)
            return cur <= h   

        while min_val <= max_val:
            mid = (min_val + max_val) // 2

            if helper(mid):
                max_val = mid - 1
                ans = mid
            else:
                min_val = mid + 1
        return ans
