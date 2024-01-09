class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        count_ones = 0
        max_len= 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count_ones += 1

            if r - l + 1 - count_ones > 1:
                if nums[l] == 1:
                    count_ones -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len - 1