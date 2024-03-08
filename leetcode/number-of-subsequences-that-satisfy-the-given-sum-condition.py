class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        ans = 0
        point = target - nums[0]
        idx = bisect_right(nums, (point))
       
        l, r = 0, min(idx, len(nums) - 1)
        while l <= r:
            if nums[r] + nums[l] > target:
                r -= 1
            else:
                val = r - l
                ans += pow(2, val)
                l += 1
        return ans % ((10**9) + 7)

