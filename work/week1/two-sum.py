class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for num in range(len(nums)):
            val = target - nums[num]
            if val in my_dict:
                return [my_dict[val], num]
            else:
                my_dict[nums[num]] = num