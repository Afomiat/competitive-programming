class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        count = 0
        res = 0
        l, r = 0, 0
        while r < len(nums):
            if nums[r] % 2 != 0:
                odd_count += 1
                count = 0
            while odd_count == k:
                count += 1
                if nums[l] % 2 != 0:
                    odd_count -= 1
                 
                l += 1
            
            res += count
            r += 1
      

        return res