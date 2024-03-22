class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            val = nums[i] - 1
            if val != i:
                if nums[i] == nums[val]:
                    res.append(nums[i])
                    i += 1
                else:
                    nums[i], nums[val] = nums[val], nums[i]
            else:
                i += 1
        return set(res)
