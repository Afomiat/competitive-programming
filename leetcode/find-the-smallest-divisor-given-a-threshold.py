class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_val = max(nums)
        min_val = 1
        ans = 0
        def helper(mid):
            cur = 0
            for i in nums:
                cur += math.ceil(i / mid)
           
            return cur <= threshold
        while min_val <= max_val:
            mid = (min_val + max_val) // 2

            if helper(mid):
                max_val = mid - 1
                ans = mid
            else:
                min_val = mid + 1

        return ans
        
      
            
