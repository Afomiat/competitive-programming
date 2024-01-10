class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        count_ones = 0
        pre_zeros = 0
        max_ones = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count_ones += 1
            else:
                pre_zeros += 1
                while pre_zeros > k:
                    if nums[l] == 0:
                        pre_zeros -= 1
                    l += 1

            max_ones = max(max_ones, r - l + 1)
        
        return max_ones