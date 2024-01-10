class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        l = 0
        rs =len(nums) + 1
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                rs= min(r - l + 1, rs)
                s -= nums[l]
                l += 1
        return 0 if rs== len(nums) + 1 else rs

       
