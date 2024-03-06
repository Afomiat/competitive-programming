class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights)
        min_cap = max(weights)
        ans = 0
        def helper(mid):
            i = 0
            for y in range(days):
                cur = 0
                while i < len(weights) and cur + weights[i] <= mid:
                    cur += weights[i]
                    i += 1
            if i >= len(weights):
                return True
            return False
        while min_cap <= max_cap:
            mid = (min_cap + max_cap) // 2

            if helper(mid):
                max_cap = mid - 1
                ans = mid
            else:
                min_cap = mid + 1


        return ans
        
