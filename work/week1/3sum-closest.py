class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        comp_sum = sum(nums[:3])
        for i in range(n - 2):
            l = i+1
            r = n-1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if abs(cur_sum - target) < abs(comp_sum - target):
                    comp_sum  = cur_sum
                if target > cur_sum:
                    l += 1
                else:
                    r -= 1
        return comp_sum
