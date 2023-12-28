class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        if all( x == nums[0] for x in nums):
            return [0] * len(nums)
        else:
            new_num = sorted(nums)
            for i in range(len(nums)):
                if nums[i] in new_num:
                    idx = new_num.index(nums[i])
                    result.append(idx)
            for i in range(len(result) - 1):
                if result[i] == result[i + 1]:
                    result[i + 1] = result[i]
                    break
        return result


